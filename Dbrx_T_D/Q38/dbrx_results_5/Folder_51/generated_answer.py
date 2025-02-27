def find_subset_of_length_n(element_set):
    if len(element_set) < 64:
        return 0
    elif len(element_set) == 64:
        return 1
    else:
        n = len(element_set)
        subsets = [element_set[i:i + 64] for i in range(n - 64 + 1)]
        return sum((1 for subset in subsets if len(subset) == 64))