def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)
    n_smallest_chars = sorted_chars[:21]
    return sorted(n_smallest_chars, reverse=True)