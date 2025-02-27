from collections import defaultdict

def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    if len(s) < 15:
        return set()
    n = 15
    palindromes = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1]:
            palindromes.add(s[i:i + n])
    return palindromes