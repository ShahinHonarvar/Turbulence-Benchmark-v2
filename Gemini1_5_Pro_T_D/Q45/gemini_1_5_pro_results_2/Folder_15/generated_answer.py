def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:3] if char.isalpha())).lower()
    return {''.join(permutation) for i in range(3, len(letters) + 1) for permutation in itertools.permutations(letters, i) if ''.join(permutation) == ''.join(reversed(''.join(permutation)))}