from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 21:
        return result
    for i in range(len(s) - 20):
        substr = s[i:i + 21]
        if len(substr) == 21 and len(''.join(set(substr))) == 21:
            result.append(''.join(substr))
    return list(set(result))