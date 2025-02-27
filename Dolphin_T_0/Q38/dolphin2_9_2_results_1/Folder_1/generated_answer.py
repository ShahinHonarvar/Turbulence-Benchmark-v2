def find_subset_of_length_n(elements):
    return len(bin(len(elements))[2:].zfill(85).replace('0', '1'))