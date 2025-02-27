import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = [c for c in s if c.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letter_counts.elements(), r // 2):
            if r % 2 == 0:
                palindrome = ''.join(combo) + ''.join(combo[::-1])
            else:
                for letter in letter_counts:
                    palindrome = ''.join(combo) + letter + ''.join(combo[::-1])
                    palindromes.add(palindrome)
    return palindromes