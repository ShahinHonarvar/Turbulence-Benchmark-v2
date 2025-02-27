from itertools import chain, combinations

def find_subset_of_length_n(set_of_elements):

    def powerset(iterable):
        xs = list(iterable)
        return chain.from_iterable((combinations(xs, n) for n in range(len(xs) + 1)))
    return sum((1 for subset in powerset(set_of_elements) if len(subset) == 41))