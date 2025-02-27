from itertools import permutations
    from collections import Counter

def palindromes_between_indices(string):
    substring = string[0:6].lower()
    letter_counts = Counter((char for char in substring if char.isalpha()))

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for length in range(6, sum(letter_counts.values()) + 1):
        for perm in permutations(letter_counts.elements(), length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes