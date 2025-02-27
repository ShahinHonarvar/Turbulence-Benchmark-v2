from itertools import combinations

def find_subset_of_length_n(set):
    """
            Finds the number of subsets of a given set of size 860.
            """
    return len(list(combinations(set, 860)))