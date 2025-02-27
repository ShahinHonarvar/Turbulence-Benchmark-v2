def find_subset_of_length_n(set_elements):
    return len(bin(sum((1 << elem for elem in set_elements)))) - 2