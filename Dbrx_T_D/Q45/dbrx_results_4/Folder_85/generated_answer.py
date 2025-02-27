import re
from collections import defaultdict

def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters = set(s)
    letter_counts = defaultdict(int, {c: s.count(c) for c in letters})
    palindromes = set()
    for length in range(7, 12):
        for combo in itertools.combinations_with_replacement(letters, length):
            if sum((letter_counts[c] for c in combo)) >= length:
                palindrome = ''.join(sorted(combo))
                palindromes.add(palindrome)
    return palindromes