import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:5] if c.isalpha()]
    letters = [c.lower() for c in letters]
    unique_letters = set(letters)
    palindromes = set()
    for r in range(2, len(unique_letters) + 1):
        for combination in itertools.combinations(unique_letters, r):
            for permutation in itertools.permutations(combination):
                p = ''.join(permutation)
                if len(p) >= 4 and p == p[::-1]:
                    palindromes.add(p)
    return palindromes