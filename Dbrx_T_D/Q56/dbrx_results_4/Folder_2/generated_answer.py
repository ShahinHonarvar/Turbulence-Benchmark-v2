from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 55):
        sublist = [s[j] for j in combinations(range(i, i + 56), 56)]
        substring = ''.join(sublist)
        if len(set(substring)) == 56:
            result.append(substring)
    return list(set(result))