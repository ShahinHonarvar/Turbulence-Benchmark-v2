def find_subset_of_length_n(set_of_elements):
    return len([subset for subset in powerset(set_of_elements) if len(subset) == 1])

def powerset(set_of_elements):
    """
    Return the powerset of a set: the set of all possible subsets.
    """
    powerset = [[]]
    for element in set_of_elements:
        powerset.extend([subset + [element] for subset in powerset])
    return powerset