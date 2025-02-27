from math import factorial

def find_subset_of_length_n(s):
    return factorial(len(s)) // (factorial(45) * factorial(len(s) - 45))