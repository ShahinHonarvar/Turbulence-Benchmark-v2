from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substring = s[3:5].lower()
    english_chars = [c for c in substring if c.isalpha()]
    palindromes = set()
    for length in range(3, len(english_chars) + 1):
        for combo in permutations(english_chars, length):
            if combo == combo[::-1]:
                palindromes.add(''.join(combo))
    return palindromes