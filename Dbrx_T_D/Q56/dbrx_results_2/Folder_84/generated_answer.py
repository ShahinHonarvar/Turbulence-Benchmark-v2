from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 112 + 1):
        c = combinations(s, i)
        for j in c:
            t = ''.join(j)
            if len(t) == 114 and len(set(t)) == 114:
                result.append(t)
    return list(set(result))