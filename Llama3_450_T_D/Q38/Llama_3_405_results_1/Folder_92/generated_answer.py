def find_subset_of_length_n(element_set):
    n = 0
    return sum((1 for subset in [{i for i in element_set if i in combination} for combination in [{j for j in element_set if len([k for k in element_set if k == j]) > index} for index in range(len(element_set))] if len(subset) == n]))