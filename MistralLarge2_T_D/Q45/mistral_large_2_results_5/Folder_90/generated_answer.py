from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substr = ''.join(filter(str.isalpha, s[:6])).lower()
    perms = set((''.join(p) for i in range(4, len(substr) + 1) for p in permutations(substr, i)))
    return {p for p in perms if is_palindrome(p)}