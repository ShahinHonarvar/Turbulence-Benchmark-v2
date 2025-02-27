def find_subset_of_length_n(elements):
    result = 2 ** len(elements)
    result -= 1
    result -= 2 ** (len(elements) - 7)
    return result