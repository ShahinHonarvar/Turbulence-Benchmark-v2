import re

def palindromes_of_specific_lengths(s):
    s = s[44:100].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for length in range(13, 43):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes