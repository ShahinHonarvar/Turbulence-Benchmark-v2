from itertools import permutations

def palindromes_between_indices(f_string):
    length = len(f_string)
    if length < 9:
        return set()
    index_2_8 = [char.lower() for char in f_string[2:9]]
    index_2_8_set = list(set(index_2_8))
    perms = set((''.join(p) for p in permutations(index_2_8_set, len(index_2_8_set))))
    result = set()
    for perm in perms:
        if len(perm) >= 4:
            if perm == perm[::-1]:
                result.add(perm)
    return result