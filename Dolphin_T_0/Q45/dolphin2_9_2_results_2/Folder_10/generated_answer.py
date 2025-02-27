import string

def palindromes_between_indices(s):
    s = ''.join([c for c in s[0:6] if c.isalpha()])
    return {s[i:j] for i in range(len(s)) for j in range(i + 2, len(s) + 1) if s[i:j] == s[i:j][::-1] and len(s[i:j]) >= 3}