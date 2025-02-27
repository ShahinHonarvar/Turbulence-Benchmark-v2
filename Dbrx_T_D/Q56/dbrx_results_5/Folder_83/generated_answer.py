from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 47):
        substr = ''.join(combinations(s[i:i + 48], 48))
        if len(set(substr)) == 48:
            result.append(substr)
    return list(set(result))