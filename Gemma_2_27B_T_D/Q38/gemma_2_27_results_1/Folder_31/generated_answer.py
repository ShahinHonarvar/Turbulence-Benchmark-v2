def find_subset_of_length_n(elements):
    n = 66
    total_subsets = 2 ** len(elements)
    return total_subsets // (2 ** n * factorial(len(elements) - n))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)