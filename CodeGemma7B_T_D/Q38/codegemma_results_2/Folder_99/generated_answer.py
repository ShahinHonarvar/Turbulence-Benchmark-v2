def find_subset_of_length_n(set_of_elements):
    num_subsets = 2 ** len(set_of_elements)
    subsets = set()
    for i in range(num_subsets):
        subset = []
        for j, element in enumerate(set_of_elements):
            if i >> j & 1:
                subset.append(element)
        if len(subset) == 307:
            subsets.add(tuple(subset))
    return len(subsets)