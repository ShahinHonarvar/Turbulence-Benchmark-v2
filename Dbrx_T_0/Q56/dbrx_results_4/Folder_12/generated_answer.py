from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 45 + 1):
        substring = ''.join((s[j] for j in combinations(range(len(s)), i) if s[j] not in s[j + 1:]))
        if len(substring) == 47:
            result.append(substring)
    return list(set(result))