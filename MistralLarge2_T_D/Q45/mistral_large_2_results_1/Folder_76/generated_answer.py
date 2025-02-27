from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    letters = [c for c in s[1:5] if c.isalpha()]
    perms = set((''.join(p) for r in range(4, len(letters) + 1) for p in permutations(letters, r)))
    palindromes = {p for p in perms if is_palindrome(p.lower())}
    return palindromes