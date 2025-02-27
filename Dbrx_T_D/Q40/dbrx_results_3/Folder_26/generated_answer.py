def return_n_smallest_chars(input_string):
    sorted_chars = sorted(list(set(input_string)))
    return sorted_chars[:43]