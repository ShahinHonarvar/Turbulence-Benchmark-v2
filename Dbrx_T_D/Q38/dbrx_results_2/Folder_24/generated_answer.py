from itertools import chain, combinations

def find_subset_of_length_n(elements):
    return chain.from_iterable((combinations(elements, n) for n in range(len(elements)) if n == 74))