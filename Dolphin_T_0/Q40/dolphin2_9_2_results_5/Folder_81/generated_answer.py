def return_n_smallest_chars(input_string):
    return sorted(input_string, key=lambda x: ord(x))[:64]