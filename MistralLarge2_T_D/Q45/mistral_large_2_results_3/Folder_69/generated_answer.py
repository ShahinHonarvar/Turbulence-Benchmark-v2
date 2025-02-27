from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = ''.join([c for c in s[:4] if c.isalpha()]).lower()
    all_permutations = set([''.join(p) for length in range(4, len(subset) + 1) for p in permutations(subset, length)])
    palindromes = {p for p in all_permutations if is_palindrome(p)}
    return palindromes