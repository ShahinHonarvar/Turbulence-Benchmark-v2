from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 143):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 144) if i <= j[0] < j[1]))
        if len(substr) == 144 and (not any((c in result for c in substr))):
            result.append(substr)
    return result