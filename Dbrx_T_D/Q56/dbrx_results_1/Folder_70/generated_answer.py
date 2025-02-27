from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 10):
        substr = [s[j] for j in combinations(range(len(s)), i) if j[-1] - j[0] == i - 1]
        if len(substr) == 12 and ''.join(substr) not in result:
            result.append(''.join(substr))
    return result