import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:8] if c.isalpha()]
    pals = set()
    for p in itertools.multiset_permutations(letters):
        for length in range(7, len(p) + 1):
            for i in range(len(p) - length + 1):
                sub = p[i:i + length]
                if sub == sub[::-1]:
                    pals.add(''.join(sub))
    return pals