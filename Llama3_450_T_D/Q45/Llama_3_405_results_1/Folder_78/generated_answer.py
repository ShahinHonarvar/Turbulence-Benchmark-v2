import itertools
from collections import Counter

def palindromes_between_indices(s):
    english_letters = [c for c in s[6:9] if c.isalpha()]
    english_letters = ''.join(english_letters).lower()
    letter_counts = Counter(english_letters)
    palindromes = set()
    for r in range(3, len(english_letters) + 1):
        for combination in itertools.combinations_with_replacement(letter_counts.elements(), r):
            combination_str = ''.join(combination)
            for p in itertools.permutations(combination_str):
                p_str = ''.join(p)
                if p_str == p_str[::-1]:
                    palindromes.add(p_str)
    return palindromes