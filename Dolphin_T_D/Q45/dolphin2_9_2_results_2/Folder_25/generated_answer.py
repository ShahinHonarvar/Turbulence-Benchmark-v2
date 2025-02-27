from itertools import permutations, combinations

def palindromes_between_indices(s):
    letters = s[1:5]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for subset in combinations(letters, r):
            for p in permutations(subset):
                pal = ''.join(p)
                if pal == pal[::-1]:
                    palindromes.add(pal.lower())
    return palindromes