from itertools import permutations as p

def palindromes_between_indices(string):
    letters = ''.join(sorted([i.lower() for i in string[1:4]]))
    if len(letters) < 4:
        return set()
    result = set()
    for arrangement in p(letters):
        result.add(''.join(arrangement))
    return result