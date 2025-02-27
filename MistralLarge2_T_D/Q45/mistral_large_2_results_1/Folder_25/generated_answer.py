from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c.lower() for c in s[1:5] if c.isalpha()]
    perms = set((''.join(p) for r in range(3, len(letters) + 1) for p in permutations(letters, r)))
    palindromes = {p for p in perms if is_palindrome(p)}
    return palindromes