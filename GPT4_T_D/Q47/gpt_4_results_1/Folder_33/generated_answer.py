import re

def palindromes_of_specific_lengths(s):
    s = s[130:296].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s) - 102):
        for j in range(i + 103, min(i + 158, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes