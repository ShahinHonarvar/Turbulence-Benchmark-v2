from itertools import combinations  # Import the combinations() function for generating subsets

def find_subset_of_length_n(set):
    return len(list(combinations(set, 66)))