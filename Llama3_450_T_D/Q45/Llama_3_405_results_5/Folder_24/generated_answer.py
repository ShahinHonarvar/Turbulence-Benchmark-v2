import itertools
from collections import Counter

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    for r in range(2, len(letters) // 2 + 1):
        for combo in itertools.combinations(letter_counts.elements(), r):
            palindrome = ''.join(combo) + ''.join(combo[::-1])
            palindromes.add(palindrome)
    return {p for p in palindromes if len(p) >= 4}