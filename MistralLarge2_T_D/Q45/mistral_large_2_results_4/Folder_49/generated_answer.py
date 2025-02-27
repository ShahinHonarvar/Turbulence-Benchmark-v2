from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    chars = [c for c in s[5:8] if c.isalpha()]
    if len(chars) < 3:
        return set()
    char_set = set(chars)
    all_permutations = set((''.join(p) for i in range(3, len(chars) + 1) for p in permutations(char_set, i)))
    palindromes = {p for p in all_permutations if len(p) >= 3 and is_palindrome(p.lower())}
    return palindromes