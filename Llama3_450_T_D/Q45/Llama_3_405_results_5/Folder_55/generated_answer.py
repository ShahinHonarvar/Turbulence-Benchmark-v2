import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:3])).lower()
    unique_letters = set(s)
    if len(unique_letters) < 3:
        return set()
    palindromes = set()
    for r in range(3, len(unique_letters) + 1):
        for combination in itertools.combinations(unique_letters, r):
            for permutation in itertools.permutations(combination):
                p = ''.join(permutation)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes