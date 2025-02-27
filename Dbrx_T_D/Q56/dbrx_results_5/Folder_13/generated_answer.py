from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 52):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 53)[i]))
        if len(substr) == 53 and len(set(substr)) == 53:
            result.append(substr)
    return list(set(result))