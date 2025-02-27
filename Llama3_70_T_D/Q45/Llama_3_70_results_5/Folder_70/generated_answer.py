import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:7])).lower()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes