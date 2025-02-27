from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 54):
        substr = ''.join((combo for combo in combinations(s[i:i + 55], 1)))
        if len(substr) == len(set(substr)):
            result.append(substr)
    return list(set(result))