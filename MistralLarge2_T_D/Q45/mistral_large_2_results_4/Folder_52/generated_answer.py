from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = ''.join(filter(str.isalpha, s[:8])).lower()
    all_permutations = set((''.join(p) for i in range(6, len(subset) + 1) for p in permutations(subset, i)))
    palindromes = {p for p in all_permutations if is_palindrome(p) and len(p) >= 6}
    return palindromes