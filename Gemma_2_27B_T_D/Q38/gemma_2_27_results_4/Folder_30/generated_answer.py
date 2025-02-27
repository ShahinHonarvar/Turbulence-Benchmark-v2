def find_subset_of_length_n(elements):
    n = 94
    total_subsets = 2 ** len(elements)
    return total_subsets - (total_subsets - fact(len(elements)) // (fact(n) * fact(len(elements) - n)))

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)