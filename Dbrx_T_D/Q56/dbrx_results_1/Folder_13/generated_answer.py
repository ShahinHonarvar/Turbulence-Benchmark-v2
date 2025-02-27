from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for j in combinations(range(len(s)), 53):
            substring = ''.join((s[k] for k in j))
            if len(substring) == len(set(substring)):
                result.append(substring)
    return list(set(result))