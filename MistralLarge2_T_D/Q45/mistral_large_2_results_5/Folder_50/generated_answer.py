from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = ''.join([c for c in s[4:9] if c.isalpha()]).lower()
    unique_chars = ''.join(set(subset))
    palindromes = set()
    for length in range(5, len(subset) + 1):
        for perm in permutations(unique_chars, length):
            word = ''.join(perm)
            if is_palindrome(word) and all((word.count(c) <= subset.count(c) for c in word)):
                palindromes.add(word)
    return palindromes