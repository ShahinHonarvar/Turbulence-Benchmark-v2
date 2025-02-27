import itertools

def palindromes_between_indices(s):
    s = [c.lower() for c in s if c.isalpha()]
    if len(s) < 7:
        return set()
    s = s[:7]
    palindromes = set()
    for p in range(len(s), 0, -1):
        for subset in itertools.combinations(s, p):
            for word in itertools.permutations(subset):
                w = ''.join(word)
                if w == w[::-1]:
                    palindromes.add(w)
    return palindromes