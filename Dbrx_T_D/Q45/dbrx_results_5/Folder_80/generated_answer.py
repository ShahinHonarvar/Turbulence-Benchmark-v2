import re
import string

def palindromes_between_indices(s):
    s = s[3:9].lower()
    s = ''.join((c for c in s if c in string.ascii_letters))
    result = set()
    for i in range(7, len(s) + 1):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                result.add(s[j:j + i])
    return result