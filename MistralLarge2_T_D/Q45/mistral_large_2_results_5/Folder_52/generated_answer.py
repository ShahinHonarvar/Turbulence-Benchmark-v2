from itertools import permutations

def palindromes_between_indices(s):
    subset = [c for c in s[:8] if c.isalpha()]
    subset = ''.join(subset).lower()
    palindromes = set()
    for length in range(6, len(subset) + 1):
        for perm in permutations(subset, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes