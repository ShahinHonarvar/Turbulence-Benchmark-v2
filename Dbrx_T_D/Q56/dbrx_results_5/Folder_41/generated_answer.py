from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(1, min(len(s), 75)):
        for perm in permutations(s, i):
            substr = ''.join(perm)
            if len(substr) == 74 and len(set(substr)) == len(substr):
                result.add(substr)
    return list(result)