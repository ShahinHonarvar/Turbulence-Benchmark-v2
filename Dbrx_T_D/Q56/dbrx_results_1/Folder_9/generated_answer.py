from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 33):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 34) if i <= j[0] < j[1]))
        if len(substr) == 34 and len(set(substr)) == 34 and (substr not in result):
            result.append(substr)
    return result