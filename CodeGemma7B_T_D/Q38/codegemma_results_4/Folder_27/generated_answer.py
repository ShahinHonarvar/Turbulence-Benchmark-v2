from itertools import combinations

def find_subset_of_length_n(elements):
    result = 0
    for sublist in combinations(elements, 56):
        result += 1
    return result