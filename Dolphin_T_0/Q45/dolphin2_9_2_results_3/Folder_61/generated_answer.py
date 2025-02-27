import itertools

def palindromes_between_indices(s):
    s = s[:8]
    palindromes = set()
    for p in range(3, len(s) + 1):
        for subset in itertools.combinations(s, p):
            for permutation in itertools.permutations(subset):
                word = ''.join(permutation)
                if word.lower() == word.lower()[::-1] and len(word) >= 7:
                    palindromes.add(word.lower())
    return palindromes