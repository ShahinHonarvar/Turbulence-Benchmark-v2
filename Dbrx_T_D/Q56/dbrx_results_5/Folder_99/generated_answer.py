from itertools import combinations

def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 110 + 1):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 110) if j[0] == i))
        if len(s) - i < 110:
            break
        if all((substring.count(c) == 1 for c in set(substring))):
            substrings.append(substring)
    return list(set(substrings))