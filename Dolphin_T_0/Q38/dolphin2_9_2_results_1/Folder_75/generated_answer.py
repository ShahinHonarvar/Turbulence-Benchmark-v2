def find_subset_of_length_n(elements):
    length = 80
    if length > len(elements):
        return 0
    num_subsets = 0
    for i in elements:
        for comb in combinations(elements, length):
            if i not in comb:
                num_subsets += 1
    return num_subsets