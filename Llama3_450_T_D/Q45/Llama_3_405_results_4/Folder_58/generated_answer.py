import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    letter_counts = Counter(letters)
    middle_letters = [letter for letter, count in letter_counts.items() if count % 2]
    first_half_letters = [letter for letter, count in letter_counts.items() for _ in range(count // 2)]
    palindromes = set()
    for r in range(3, len(first_half_letters) + 1):
        for first_half in itertools.permutations(first_half_letters, r):
            palindrome = ''.join(first_half) + (middle_letters[0] if middle_letters else '') + ''.join(first_half[::-1])
            palindromes.add(palindrome)
    return palindromes