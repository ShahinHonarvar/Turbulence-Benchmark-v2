from string import ascii_letters as letters
    from itertools import combinations

def palindromes_between_indices(s):
    if not isinstance(s, str):
        return {}
    s = s[3:10]
    s = ''.join((ch for ch in s if ch in letters))
    s = s.lower()
    if len(s) < 5:
        return set()

    def is_palindrome(s):
        return s == s[::-1]
    res = set()
    for comb in combinations(s, 5):
        if is_palindrome(''.join(comb)):
            res.add(''.join(comb))
    return res