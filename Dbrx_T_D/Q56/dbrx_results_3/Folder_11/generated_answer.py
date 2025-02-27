from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 77):
        for perm in permutations(s[i:i + 78]):
            t = ''.join(perm)
            if len(t) == len(set(t)) and len(t) == 78:
                result.add(t)
    return list(result)