import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combination in itertools.combinations(letters, r):
            for permutation in itertools.permutations(combination):
                p = ''.join(permutation)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes