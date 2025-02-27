import re

def palindromes_of_specific_lengths(s):
    s = re.sub('[^a-zA-Z]', '', s[:101]).lower()
    palindromes = set()
    n = len(s)
    for length in range(3, 16):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes