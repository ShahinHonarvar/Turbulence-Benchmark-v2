from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 112 + 1):
        for j in combinations(range(len(s)), i):
            if len(''.join((s[k] for k in j))) == 114 and len(set(''.join((s[k] for k in j)))) == 114:
                result.append(''.join((s[k] for k in j)))
    return list(set(result))