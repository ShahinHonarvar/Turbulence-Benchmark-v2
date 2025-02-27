import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letter_counts.elements(), r):
            if len(combo) % 2 == 1:
                combo_counts = Counter(combo)
                center_counts = combo_counts - Counter({k: v // 2 * 2 for k, v in combo_counts.items()})
                if len(center_counts) > 1 or list(center_counts.values())[0] > 1:
                    continue
                first_half = ''.join(combo[:len(combo) // 2])
                second_half = first_half[::-1]
                palindrome = first_half + ''.join(center_counts.elements()) + second_half
                palindromes.add(palindrome)
            else:
                combo_counts = Counter(combo)
                if any((v % 2 != 0 for v in combo_counts.values())):
                    continue
                first_half = ''.join(combo[:len(combo) // 2])
                second_half = first_half[::-1]
                palindrome = first_half + second_half
                palindromes.add(palindrome)
    return palindromes