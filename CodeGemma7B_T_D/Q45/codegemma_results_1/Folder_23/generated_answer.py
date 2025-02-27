from itertools import permutations

def palindromes_between_indices(my_string):
    result = set()
    for p in permutations(my_string[0:7].lower()):
        if ''.join(p) == ''.join(p[-2::-1]):
            result.add(''.join(p))
    return result