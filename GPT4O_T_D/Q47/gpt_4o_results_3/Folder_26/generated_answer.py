import re

def palindromes_of_specific_lengths(s):
    s = s[24:85]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    n = len(s)
    result = set()
    for length in range(21, 32):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result