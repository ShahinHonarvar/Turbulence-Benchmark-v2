from itertools import combinations

def find_subset_of_length_n(elements):
    count = 0
    for i in combinations(elements, 84):
        count += 1
    return count