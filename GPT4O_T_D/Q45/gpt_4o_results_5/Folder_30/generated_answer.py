from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[:5].lower()
    filtered_s = ''.join(filter(str.isalpha, s))
    if len(filtered_s) < 4:
        return set()
    perms = set(permutations(filtered_s))
    palindromes = {''.join(p) for p in perms if is_palindrome(p)}
    return {p for p in palindromes if len(p) >= 4}