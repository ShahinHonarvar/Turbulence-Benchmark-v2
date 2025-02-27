from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 11):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 12) if i <= j[0] < j[1]))
        if len(substring) == 12 and len(set(substring)) == 12 and (substring not in result):
            result.append(substring)
    return result