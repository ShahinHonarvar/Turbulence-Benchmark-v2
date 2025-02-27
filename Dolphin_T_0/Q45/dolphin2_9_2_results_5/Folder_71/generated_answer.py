import itertools

def palindromes_between_indices(word):
    characters = [char for char in word.lower() if char.isalpha()]
    if not 1 <= len(characters) <= 3:
        return set()
    permutations = set((''.join(p) for i in range(2, len(characters) + 1) for p in itertools.permutations(characters, i)))
    palindromes = set()
    for permutation in permutations:
        if permutation == permutation[::-1] and len(permutation) >= 4:
            palindromes.add(permutation)
    return palindromes_between_indices