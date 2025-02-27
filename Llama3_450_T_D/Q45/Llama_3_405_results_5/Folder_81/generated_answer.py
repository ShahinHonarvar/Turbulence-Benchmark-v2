import itertools
from collections import Counter

def palindromes_between_indices(s):
    english_letters = [c for c in s[:7].lower() if c.isalpha()]
    letter_counts = Counter(english_letters)
    palindromes = set()
    for r in range(3, len(english_letters) + 1):
        for combo in itertools.combinations(english_letters, r):
            combo_counts = Counter(combo)
            if all((combo_counts[c] <= letter_counts[c] for c in combo)):
                palindrome = ''.join(combo) + ''.join(combo[:-1][::-1])
                palindromes.add(palindrome)
    return palindromes