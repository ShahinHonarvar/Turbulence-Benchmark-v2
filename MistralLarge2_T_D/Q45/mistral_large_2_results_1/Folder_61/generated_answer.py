from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = ''.join((c for c in s[:8] if c.isalpha())).lower()
    palindromes = set()
    for length in range(7, len(subset) + 1):
        for perm in permutations(subset, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes