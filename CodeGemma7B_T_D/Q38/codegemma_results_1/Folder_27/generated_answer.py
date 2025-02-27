from itertools import combinations

def find_subset_of_length_n(arr):
    count = 0
    for subset in combinations(arr, n):
        count += 1
    return count