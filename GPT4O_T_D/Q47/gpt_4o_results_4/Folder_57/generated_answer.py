import re

def palindromes_of_specific_lengths(s):
    s = s[16:95].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 39, min(len(s), start + 53)):
            substring = s[start:end + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes