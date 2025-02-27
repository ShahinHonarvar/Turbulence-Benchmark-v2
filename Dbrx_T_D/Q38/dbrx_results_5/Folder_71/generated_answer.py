from math import factorial

def find_subset_of_length_n(elements_set):
    if not isinstance(elements_set, set) or len(elements_set) < 78:
        return 0
    return int(factorial(len(elements_set)) / (factorial(78) * factorial(len(elements_set) - 78)))