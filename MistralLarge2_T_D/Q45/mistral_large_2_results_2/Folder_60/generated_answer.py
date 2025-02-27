from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[3:7])).lower()
    perms = set((''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i)))
    return {p for p in perms if is_palindrome(p) and len(p) >= 4}