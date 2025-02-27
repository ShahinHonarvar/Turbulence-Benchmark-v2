import itertools, string

def palindromes_between_indices(string):
    indices = range(0, 6)
    letters = [s.lower() for s in list(string) if s.isalpha()]
    subsets = [set(itertools.permutations(letters, i)) for i in indices]
    palindromes = set()
    for subset in subsets:
        for s in subset:
            pal = ''.join(s)
            if pal == pal[::-1] and len(pal) >= 5:
                palindromes.add(pal.lower())
    return palindromes