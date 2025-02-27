def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string, key=ord)
    sorted_n_chars = sorted_chars[:-28:-1]
    return sorted_n_chars