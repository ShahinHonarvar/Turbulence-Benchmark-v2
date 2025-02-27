from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    """
            This function takes a set of elements as input and returns the number of all its subsets of size n.
            """
    return len(list(combinations(set_of_elements, 38)))