def return_n_smallest_chars(input_string):
    smallest_chars = sorted(set(input_string))[:35]
    return sorted(smallest_chars, reverse=True)