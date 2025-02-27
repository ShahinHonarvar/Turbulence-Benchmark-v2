from math import factorial

def find_subset_of_length_n(elements):
    n = 4
    combinations = len(elements) // n
    if len(elements) < n:
        return 0
    return factorial(len(elements)) / (factorial(n) * factorial(len(elements) - n))