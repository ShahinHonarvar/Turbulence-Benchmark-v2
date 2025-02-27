def find_subset_of_length_n(elements_set, length):
    if length == 1:
        return elements_set
    subset = set()
    for element in elements_set:
        subset.add(frozenset([element]))
    for i in range(1, length):
        for j in range(i, length):
            for subset_i in list(subset)[:]:
                for element in elements_set - subset_i:
                    new_subset = subset_i | frozenset([element])
                    if len(new_subset) > j:
                        break
                    if len(new_subset) == j:
                        subset.add(new_subset)
    return subset

def count_subsets_of_length_n(elements_set, length):
    if length == 0:
        return 0
    if length > len(elements_set):
        return 0
    subset = find_subset_of_length_n(elements_set, length)
    return len(subset)