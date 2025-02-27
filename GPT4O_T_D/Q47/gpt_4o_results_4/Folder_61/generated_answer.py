import re

def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    n = len(s)
    for length in range(20, 31):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes