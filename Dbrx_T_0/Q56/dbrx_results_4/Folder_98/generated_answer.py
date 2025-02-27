from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 9):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 10)[i]))
        if len(substr) == 10 and len(set(substr)) == 10:
            result.append(substr)
    return list(set(result))