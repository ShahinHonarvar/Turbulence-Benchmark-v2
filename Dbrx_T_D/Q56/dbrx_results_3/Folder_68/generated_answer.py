from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 74):
        substring = ''.join((c for j, c in enumerate(s[i:i + 75]) if j in combinations(range(75), 75 - 1)))
        if substring and substring not in result:
            result.append(substring)
    return result