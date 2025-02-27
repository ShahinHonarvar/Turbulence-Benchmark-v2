import itertools

def palindromes_between_indices(string):
    string = string.lower()
    substring = string[1:7]
    permutations = set()
    for permutation in itertools.permutations(substring):
        permutations.add(''.join(permutation))
    palindromes = set()
    for permutation in permutations:
        if permutation == permutation[::-1] and len(permutation) >= 5:
            palindromes.add(permutation)
    return palindromes