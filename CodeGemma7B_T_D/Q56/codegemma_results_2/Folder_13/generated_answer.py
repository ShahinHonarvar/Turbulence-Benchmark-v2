from itertools import combinations

def all_substring_of_size_n(str):
    combi = [''.join(c) for c in combinations(map(str, range(len(str))), 53)]
    return list({c for c in combi if len(set(c)) == 53})