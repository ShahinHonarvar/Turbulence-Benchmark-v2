def palindromes_between_indices(string):
    string = string.lower()
    substring = string[0:8]
    if len(set(substring)) < 7:
        return set()
    permutations = permutations(substring)
    palindromes = set()
    for permutation in permutations:
        if permutation == permutation[::-1]:
            palindromes.add(''.join(permutation))
    return palindromes