def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    smallest_chars = sorted_chars[:64]
    return sorted(smallest_chars, reverse=True)