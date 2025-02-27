from itertools import permutations

def palindromes_between_indices(s):
    subset = ''.join(filter(str.isalpha, s[:5])).lower()
    unique_letters = set(subset)
    palindromes = set()
    for length in range(4, len(subset) + 1):
        for perm in permutations(subset, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes