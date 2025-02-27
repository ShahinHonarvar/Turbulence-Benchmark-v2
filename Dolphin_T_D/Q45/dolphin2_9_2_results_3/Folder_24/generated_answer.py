import math
import string

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = set(s)
    n = len(s)
    palindromes = set()
    for length in range(4, n + 1):
        for start in range(0, n - length + 1):
            substr = s[start:start + length]
            if set(substr) <= letters and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes