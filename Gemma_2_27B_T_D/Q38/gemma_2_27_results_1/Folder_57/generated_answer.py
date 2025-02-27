def find_subset_of_length_n(elements):
    n = 92
    total_subsets = 2 ** len(elements)
    subsets_of_length_n = total_subsets if n == len(elements) else 0
    if n < len(elements):
        subsets_of_length_n = factorial(len(elements)) / (factorial(n) * factorial(len(elements) - n))
    return subsets_of_length_n

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)