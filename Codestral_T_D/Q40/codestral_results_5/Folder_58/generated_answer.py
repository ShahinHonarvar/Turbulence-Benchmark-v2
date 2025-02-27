def return_n_smallest_chars(input_str):
    sorted_chars = sorted(list(input_str))
    smallest_chars = sorted_chars[:49]
    return sorted(smallest_chars, reverse=True)