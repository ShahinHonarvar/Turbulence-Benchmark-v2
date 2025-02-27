from itertools import combinations

def find_subset_of_length_n(s):
    count = 0
    for i in combinations(s, 95):
        count += 1
    return count