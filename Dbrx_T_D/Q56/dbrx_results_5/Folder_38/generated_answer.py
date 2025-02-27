from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 34):
        substring = ''.join((x for j, x in enumerate(s[i:i + 35]) if j in combinations(range(35), 1)))
        if len(set(substring)) == 35:
            result.append(substring)
    return list(set(result))