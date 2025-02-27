def return_n_smallest_chars(input_string):
    ascii_values = sorted(list(set(input_string)), reverse=True)
    return [chr(ascii) for ascii in ascii_values][:45]