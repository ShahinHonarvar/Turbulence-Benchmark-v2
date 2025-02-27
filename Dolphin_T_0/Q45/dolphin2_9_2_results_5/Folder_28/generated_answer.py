from itertools import permutations, combinations

def palindromes_between_indices(s):
    subset = s[1:6]
    palindromes = set()
    for length in range(4, len(subset) + 1):
        for perm in permutations(subset, length):
            word = ''.join(perm).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes