from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 37:
        return result
    for i in range(len(s) - 36):
        for perm in permutations(s[i:i + 37], 37):
            t = ''.join(perm)
            if len(t) == 37 and all((t.count(c) == 1 for c in t)):
                result.append(t)
                break
    return list(set(result))