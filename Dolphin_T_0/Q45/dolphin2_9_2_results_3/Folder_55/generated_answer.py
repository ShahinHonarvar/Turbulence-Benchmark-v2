from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(s):
    indices = [0, 1, 2]
    subset = [s[i] for i in indices]
    subset = [i for i in subset if i in ascii_letters]
    palindromes = set()
    for i in range(3, len(subset) + 1):
        subset_combinations = permutations(subset, i)
        for combination in subset_combinations:
            combination = ''.join(combination).lower()
            if combination == combination[::-1]:
                palindromes.add(combination)
    return palindromes