from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 56):
        substring = ''.join((s[j] for j in combinations(range(len(s)), i) if s[j] not in s[j + 1:]))
        if len(substring) == 57 and substring not in result:
            result.append(substring)
    return result