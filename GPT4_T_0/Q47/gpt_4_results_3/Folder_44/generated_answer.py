import re

def palindromes_of_specific_lengths(s):
    s = s[18:99]
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 31, min(i + 52, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes