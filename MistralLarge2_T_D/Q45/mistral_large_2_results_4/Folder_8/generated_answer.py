from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join(filter(str.isalpha, s[1:6])).lower()
    perms = set((''.join(p) for i in range(5, len(substring) + 1) for p in permutations(substring, i)))
    palindromes = {p for p in perms if is_palindrome(p)}
    return palindromes