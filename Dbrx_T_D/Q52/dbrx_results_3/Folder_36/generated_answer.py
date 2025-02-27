import re
from collections import defaultdict

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s.lower())
    n = 338
    if len(s) < n:
        return set()
    palindromes = set()
    for i in range(len(s) - n + 1):
        pal = s[i:i + n]
        if pal == pal[::-1]:
            palindromes.add(pal)
    return palindromes