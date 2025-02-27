from itertools import combinations

def all_substring_of_size_n(s):
    substrings = []
    for i in combinations(range(len(s)), 35):
        substring = s[i[0]:i[-1] + 1]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return list(set(substrings))