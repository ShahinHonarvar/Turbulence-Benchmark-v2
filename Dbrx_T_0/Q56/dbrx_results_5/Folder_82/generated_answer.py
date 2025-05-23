from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 100):
        substr = ''.join((s[j] for j in combinations(range(len(s)), i) if s[j] not in s[j + 1:]))
        if len(substr) == 100 and substr not in result:
            result.append(substr)
    return result