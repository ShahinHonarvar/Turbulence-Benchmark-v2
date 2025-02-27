def find_subset_of_length_n(elements):
    subsets_of_length_n = []
    for i in elements:
        if len(i) == 97:
            subsets_of_length_n.append(i)
    return len(subsets_of_length_n)