import itertools
from collections import Counter

def palindromes_between_indices(s):
    letters = [c for c in s[1:6].lower() if c.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letter_counts.elements(), r):
            combo_str = ''.join(combo)
            if combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes