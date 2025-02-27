from collections import Counter
from itertools import combinations_with_replacement

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    letter_counts = Counter(letters)
    result = set()
    for combo in combinations_with_replacement(letter_counts.keys(), 6):
        combo_counts = Counter(combo)
        if all((combo_counts[c] <= letter_counts[c] for c in combo)):
            palindrome = ''.join(combo + combo[:-1][::-1])
            result.add(palindrome)
    return result