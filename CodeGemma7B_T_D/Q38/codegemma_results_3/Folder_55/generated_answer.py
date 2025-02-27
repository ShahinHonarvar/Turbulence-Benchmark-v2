def find_subset_of_length_n(set_of_elements):
    subsets = []
    for i in range(2 ** len(set_of_elements)):
        subset = []
        for j in range(len(set_of_elements)):
            if i & 1 << j:
                subset.append(set_of_elements[j])
        subsets.append(subset)
    return len([s for s in subsets if len(s) == n])