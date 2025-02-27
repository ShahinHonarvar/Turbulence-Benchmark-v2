def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:7] if char.isalpha())).lower()
    return {''.join(permutation) for i in range(3, len(letters) + 1) for permutation in set(itertools.permutations(letters, i)) if ''.join(permutation) == ''.join(reversed(''.join(permutation)))}