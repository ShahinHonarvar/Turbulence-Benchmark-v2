def find_subset_of_length_n(elements):
    n = 69
    return sum((1 for i in range(len(elements)) if len(elements.difference(set(list(itertools.combinations(elements, i))))) == n))