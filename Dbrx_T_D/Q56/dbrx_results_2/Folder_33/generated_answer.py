from itertools import combinations

def all_substrings_of_size_n(s):
    result = []
    if len(s) < 105:
        return result
    for i in range(len(s) - 104):
        for j in combinations(range(i, len(s)), 105):
            t = ''.join((s[index] for index in j))
            if len(t) == len(set(t)):
                result.append(t)
    return list(set(result))