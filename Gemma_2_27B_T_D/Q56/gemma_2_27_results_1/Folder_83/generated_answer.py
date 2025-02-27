from itertools import combinations

def all_substring_of_size_n(s):
    return list({''.join(c) for i in range(len(s) - 47) for c in combinations(s[i:i + 48], 48) if len(set(c)) == 48})