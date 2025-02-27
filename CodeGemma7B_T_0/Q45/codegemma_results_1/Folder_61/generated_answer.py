from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower()
    letters = [char for char in text if char.isalpha()]
    if len(letters) < 7:
        return set()
    permutations_list = list(permutations(letters[0:8]))
    palindromes = set()
    for permutation in permutations_list:
        if permutation == permutation[::-1]:
            palindromes.add(''.join(permutation))
    return palindromes