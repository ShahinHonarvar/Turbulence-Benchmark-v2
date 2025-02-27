from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 5):
        for j in combinations(range(len(s)), 6):
            substring = ''.join((s[k] for k in j if k >= i and k < i + 6))
            if len(substring) == 6 and len(set(substring)) == 6:
                result.append(substring)
    return list(set(result))