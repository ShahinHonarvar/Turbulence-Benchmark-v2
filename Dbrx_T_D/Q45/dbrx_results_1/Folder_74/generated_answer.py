from itertools import permutations

def palindromes_between_indices(s):
    english_letters = {c.lower() for c in s if c.isalpha()}
    if len(english_letters) < 6:
        return set()
    english_letters = ''.join(sorted(english_letters))
    palindromes = set()
    for perm in permutations(english_letters, 6):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes