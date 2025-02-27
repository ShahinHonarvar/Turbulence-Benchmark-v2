import itertools

def palindromes_between_indices(string):
    substring = string[:6]
    combinations = []
    for i in range(len(substring) + 1):
        combinations += list(itertools.combinations(substring, i))
    combinations = [''.join(combination) for combination in combinations]
    permutations = []
    for combination in combinations:
        permutations += [''.join(permutation) for permutation in itertools.permutations(combination)]
    palindromes = []
    for permutation in permutations:
        if len(permutation) >= 3 and permutation.lower() == permutation.lower()[::-1]:
            palindromes.append(permutation)
    return set(palindromes)