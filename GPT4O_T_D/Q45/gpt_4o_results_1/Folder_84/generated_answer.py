from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[4:10].lower()
    alpha_chars = [c for c in s if c.isalpha()]
    res = set()
    if len(alpha_chars) == 0:
        return res
    for n in range(3, len(alpha_chars) + 1):
        for perm in permutations(alpha_chars, n):
            word = ''.join(perm)
            if is_palindrome(word):
                res.add(word)
    return res