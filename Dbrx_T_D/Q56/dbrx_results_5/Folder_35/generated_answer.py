from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 26):
        substr = ''.join((x for x in combinations(s[i:i + 27], 1)))
        if len(substr) == 27 and all((substr.count(c) == 1 for c in set(substr))):
            result.append(substr)
    return list(set(result))