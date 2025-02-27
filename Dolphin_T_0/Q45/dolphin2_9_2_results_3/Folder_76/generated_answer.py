from itertools import permutations

def palindromes_between_indices(input_string):
    letters = input_string[1:5]
    palindromes = {''.join(x).lower() for x in chains.from_iterable(permutations(letters, r=4)) if ''.join(x).lower() == ''.join(x).lower()[::-1]}
    return set(palindromes)