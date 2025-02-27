from itertools import combinations

def find_subset_of_length_n(elements):
    """
            This function takes one argument, a set of elements, and returns the number of all its subsets of size 449.
            """
    num_subsets = []
    for combination in combinations(elements, 449):
        num_subsets.append(len(combination))
    return len(num_subsets)