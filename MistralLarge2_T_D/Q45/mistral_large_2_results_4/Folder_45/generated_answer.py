from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join((c.lower() for c in s[5:10] if c.isalpha()))
    perms = set(permutations(letters, r))
    palindromes = {''.join(perm) for r in range(4, len(letters) + 1) for perm in perms if is_palindrome(perm)}
    return palindromes