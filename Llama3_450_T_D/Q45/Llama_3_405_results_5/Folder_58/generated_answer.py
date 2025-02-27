import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letter_counts.elements(), r):
            combo_counts = Counter(combo)
            if len(combo_counts) > 1 and all((combo_counts[c] % 2 == 0 for c in combo_counts)):
                palindrome = ''.join(combo)
                palindromes.add(palindrome)
    return palindromes