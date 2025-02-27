def find_subset_of_length_n(input_set):
    total_subsets = 2 ** len(input_set)
    subsets_of_length_n = total_subsets - total_subsets // 2 - total_subsets // 2 // 2 - total_subsets // 2 // 4 - total_subsets // 2 // 8 - total_subsets // 2 // 16 - total_subsets // 2 // 32 - total_subsets // 2 // 64
    return subsets_of_length_n