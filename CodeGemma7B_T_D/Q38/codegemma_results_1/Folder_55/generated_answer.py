from itertools import combinations

def find_subset_of_length_n(set):
    count = 0
    for item in combinations(set, 21):
        count += 1
    return count