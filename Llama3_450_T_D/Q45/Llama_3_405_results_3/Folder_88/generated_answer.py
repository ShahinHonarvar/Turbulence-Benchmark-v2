import itertools
from collections import Counter

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letter_counts.elements(), r):
            if len(combo) >= 6:
                palindrome = ''.join(combo) + ''.join(combo[::-1][1:])
                palindromes.add(palindrome)
    return palindromes