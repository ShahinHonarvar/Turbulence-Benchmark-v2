from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    letters = list(string[7:10])
    permutations_of_letters = permutations(letters)
    palindromes = set()
    for permutation in permutations_of_letters:
        if len(''.join(permutation)) >= 4:
            palindromes.add(''.join(permutation))
    return palindromes