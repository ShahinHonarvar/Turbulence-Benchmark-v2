from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:10].lower()
    palindromes = set()
    for length in range(3, len(s) + 1):
        for p in permutations(s, length):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes