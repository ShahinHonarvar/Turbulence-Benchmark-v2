def find_subset_of_length_n(elements):
    total_subsets = 2 ** len(elements)
    subsets_of_length_n = [s for s in range(total_subsets) if bin(s).count('1') == 94]
    return len(subsets_of_length_n)