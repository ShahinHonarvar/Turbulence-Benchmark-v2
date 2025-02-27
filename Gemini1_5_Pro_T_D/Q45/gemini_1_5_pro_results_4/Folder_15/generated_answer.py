def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:3] if char.isalpha())).lower()
    return {permutation for i in range(3, len(letters) + 1) for permutation in ''.join(p) for p in itertools.permutations(letters, i) if permutation == permutation[::-1]}