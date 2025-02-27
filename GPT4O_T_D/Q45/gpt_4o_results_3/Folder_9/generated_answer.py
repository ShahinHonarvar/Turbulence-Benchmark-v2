from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    s = ''.join(filter(str.isalpha, s[:7]))
    perms = set((''.join(p) for p in permutations(s) if len(p) >= 7))
    return {p for p in perms if is_palindrome(p)}