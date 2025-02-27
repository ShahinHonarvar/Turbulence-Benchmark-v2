import re
from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    chars = s[4:8]
    chars = ''.join(filter(str.isalpha, chars))
    if len(chars) < 5:
        return set()
    palindromes = set()
    for i in range(len(chars)):
        for j in range(i, len(chars)):
            substring = chars[i:j + 1]
            if len(substring) >= 5 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes