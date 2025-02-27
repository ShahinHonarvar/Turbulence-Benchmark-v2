def return_n_smallest_chars(input_string):
    smallest_chars = sorted(input_string)[:6]
    return sorted(smallest_chars, reverse=True)