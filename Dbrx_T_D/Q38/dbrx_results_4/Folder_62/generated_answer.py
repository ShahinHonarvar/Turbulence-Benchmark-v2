from itertools import chain, combinations

def find_subset_of_length_n(elements):
    return len(list(chain.from_iterable((combinations(elements, i) for i in range(86, 87)))))