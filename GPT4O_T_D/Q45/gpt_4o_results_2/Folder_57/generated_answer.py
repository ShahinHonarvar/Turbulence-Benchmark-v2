from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    sub_str = ''.join([char for char in s[2:6] if char.isalpha()]).lower()
    if len(sub_str) < 5:
        return set()
    perm_set = set((''.join(p) for p in permutations(sub_str, 5)))
    palindrome_set = {p for p in perm_set if is_palindrome(p)}
    return palindrome_set