def find_subset_of_length_n(elements):
    result = bin(2 ** len(elements))[2:]
    return int(result, 2)