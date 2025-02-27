def find_subset_of_length_n(set_of_elements):
    return len(bin(sum((1 << i for i in set_of_elements)))) - 2