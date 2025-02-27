def return_n_smallest_chars(input_string):
    ascii_values = sorted(list(set(input_string)), reverse=True)
    return [chr(i) for i in ascii_values[:65]]