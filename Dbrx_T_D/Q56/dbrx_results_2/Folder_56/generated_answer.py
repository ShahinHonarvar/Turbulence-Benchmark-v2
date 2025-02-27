from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 68):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 69)[i]))
        if len(substring) == 69 and len(set(substring)) == 69:
            result.append(substring)
    return list(set(result))