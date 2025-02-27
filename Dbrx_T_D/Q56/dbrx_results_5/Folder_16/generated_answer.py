from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 124):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 124) if i <= j < i + 124))
        if len(set(substr)) == 124:
            result.append(substr)
    return list(set(result))