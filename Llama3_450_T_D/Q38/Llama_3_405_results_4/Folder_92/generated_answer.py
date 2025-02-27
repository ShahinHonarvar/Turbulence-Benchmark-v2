def find_subset_of_length_n(element_set):
    n = 0
    return len([subset for subset in [{i for i in element_set if i in combination} for combination in [{i for i in element_set if element_set.index(i) < element_set.index(element)} for element in element_set]] if len(subset) == n])