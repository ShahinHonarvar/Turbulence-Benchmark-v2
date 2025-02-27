from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    substring = s[4:6].lower()
    english_letters = ''.join((c for c in substring if c.isalpha()))
    palindromes = set()
    for length in range(3, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes