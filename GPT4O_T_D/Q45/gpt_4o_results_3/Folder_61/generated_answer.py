from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    english_letters = ''.join([c for c in s if c.isalpha()])
    palindromes = set()
    for length in range(7, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes