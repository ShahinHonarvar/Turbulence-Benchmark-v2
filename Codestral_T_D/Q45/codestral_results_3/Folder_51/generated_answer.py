from itertools import permutations

def palindromes_between_indices(s):
    subset = s[3:6]
    subset = subset.lower()
    palindromes = set()
    for i in range(3, len(subset) + 1):
        for perm in permutations(subset, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes