import string
    from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join([_ for _ in s[:7] if _ in string.ascii_lowercase])
    is_palindrome = lambda s: s == s[::-1]
    return set([''.join(p) for p in permutations(s) if len(''.join(p)) >= 3 and is_palindrome(''.join(p))])