from itertools import permutations

def palindromes_between_indices(str):
    str = str.lower()
    letters_between_indices = str[2:4]
    if len(letters_between_indices) >= 3:
        permutations_of_letters = permutations(letters_between_indices)
        palindromes = {''.join(p) for p in permutations_of_letters}
        return palindromes
    else:
        return set()