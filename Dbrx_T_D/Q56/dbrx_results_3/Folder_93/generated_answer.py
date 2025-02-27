from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for j in combinations(range(len(s)), 54):
            substring = ''.join((s[k] for k in j if k >= i and k <= i + 53))
            if len(substring) == 54 and len(set(substring)) == 54:
                result.append(substring)
    return list(set(result))