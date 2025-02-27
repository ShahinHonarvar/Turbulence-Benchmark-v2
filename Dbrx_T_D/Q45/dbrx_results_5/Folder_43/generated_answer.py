import itertools

def palindromes_between_indices(s):
    english_letters = frozenset('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    slice_letters = set(english_letters.intersection(s[2:6]))
    if len(slice_letters) < 2:
        return set()
    palindromes = set()
    for n in range(4, 1 + len(slice_letters)):
        for combo in itertools.combinations(slice_letters, n):
            candidate = ''.join(combo)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes