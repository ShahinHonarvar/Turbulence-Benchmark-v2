def find_subset_of_length_n(elements):
    return sum((1 for i in range(len(elements)) if len(set(combinations(elements, i))) == 8))