from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 91):
        substring = ''.join((s[j] for j in combinations(range(len(s)), i) if len(s[j]) == 92 and len(set(s[j])) == len(s[j])))
        result.append(substring)
    return list(set(result))