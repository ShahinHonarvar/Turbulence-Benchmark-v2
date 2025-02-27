from itertools import permutations

def palindromes_between_indices(s):
    subset = [c for c in s[6:9] if c.isalpha()]
    subset = [c.lower() for c in subset]
    palindromes = set()
    for length in range(4, len(subset) + 1):
        for perm in permutations(subset, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes