def return_n_smallest_chars(input_string):
    ascii_list = sorted(list(set(input_string)), reverse=True)
    return ascii_list[:28]