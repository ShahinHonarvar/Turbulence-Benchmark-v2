from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 51):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 52) if s[j] in s[i:i + 52]))
        if len(set(substr)) == 52:
            result.append(substr)
    return list(set(result))