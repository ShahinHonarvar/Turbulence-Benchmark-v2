from itertools import combinations

def find_subset_of_length_n(s):
    subsets = combinations(s, 57)
    count = 0
    for _ in subsets:
        count += 1
    return count