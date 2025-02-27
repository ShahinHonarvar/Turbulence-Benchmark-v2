def find_subset_of_length_n(element_set):
    if len(element_set) < 722:
        return 0
    return int(factorial(len(element_set)) / (factorial(722) * factorial(len(element_set) - 722)))