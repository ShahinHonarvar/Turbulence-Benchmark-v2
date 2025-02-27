import itertools

def palindromes_between_indices(s):
    s = s[:8].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(4, len(s) + 1):
        for p in itertools.permutations(s, length):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes