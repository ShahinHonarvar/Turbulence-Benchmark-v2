from itertools import combinations

def find_subset_of_length_n(s):
    length = 40
    count = 0
    for c in combinations(s, length):
        count += 1
    return count