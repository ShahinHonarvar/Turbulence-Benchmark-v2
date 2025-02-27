def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)
    smallest_chars = sorted_chars[:59]
    return sorted(smallest_chars, reverse=True)