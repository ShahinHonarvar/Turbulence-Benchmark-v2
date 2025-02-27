from itertools import permutations

def palindromes_between_indices(s):
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    english_chars = set((c.lower() for c in s if c.lower() in valid_chars))
    if len(english_chars) < 6:
        return set()
    palindromes = set()
    for perm in permutations(english_chars, 6):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes