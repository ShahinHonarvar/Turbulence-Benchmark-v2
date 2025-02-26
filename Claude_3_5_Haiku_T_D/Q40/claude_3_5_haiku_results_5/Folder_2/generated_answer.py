def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))[:48]
    return sorted_chars