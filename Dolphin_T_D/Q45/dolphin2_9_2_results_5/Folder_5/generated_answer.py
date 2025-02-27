import itertools

def palindromes_between_indices(s):
    between = s[4:9]
    palindromes = set()
    for p in range(4, len(between) + 1):
        for c in itertools.combinations(between, p):
            perm = list(itertools.permutations(c))
            for p in perm:
                word = ''.join(p).lower()
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes