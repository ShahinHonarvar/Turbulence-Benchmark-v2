import itertools
from collections import Counter

def palindromes_between_indices(s):
    letters = [c for c in s[2:6] if c.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    for r in range(4, sum(letter_counts.values()) + 1):
        for combo in itertools.combinations_with_replacement(letter_counts.elements(), r):
            combo_counts = Counter(combo)
            if all((combo_counts[c] <= letter_counts[c] for c in combo_counts)):
                palindrome = ''.join(combo)
                if palindrome == palindrome[::-1].lower():
                    palindromes.add(palindrome.lower())
    return palindromes