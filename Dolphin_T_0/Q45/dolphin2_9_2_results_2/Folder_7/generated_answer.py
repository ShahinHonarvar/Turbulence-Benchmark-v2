import itertools

def palindromes_between_indices(s):
    s = s[1:10]
    palindromes = set()
    for p in range(7, len(s) + 1):
        for subset in itertools.combinations(s, p):
            for arrangement in itertools.permutations(subset):
                word = ''.join(arrangement).lower()
                if word == word[::-1] and len(word) >= 7:
                    palindromes.add(word)
    return palindromes