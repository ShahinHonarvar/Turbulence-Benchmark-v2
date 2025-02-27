from math import factorial

def find_subset_of_length_n(set_of_elements):
    """Given a set of elements, returns the number of all its subsets of size n."""
    return int(factorial(len(set_of_elements)) / (factorial(len(set_of_elements) - 180) * factorial(180)))