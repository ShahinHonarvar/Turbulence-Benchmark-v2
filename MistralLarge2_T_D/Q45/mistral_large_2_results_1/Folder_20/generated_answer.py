from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join((c for c in s[2:9] if c.isalpha())).lower()
    perms = set((''.join(p) for p in permutations(substring)))
    palindromes = {p for p in perms if is_palindrome(p) and len(p) >= 4}
    return palindromes