from itertools import combinations

def find_subset_of_length_n(input_set):
    count = 0
    for i in combinations(input_set, 88):
        count += 1
    return count