from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    for i in permutations(s[2:6]):
        i = ''.join(i)
        if i == i[::-1]:
            result.add(i)
    return result