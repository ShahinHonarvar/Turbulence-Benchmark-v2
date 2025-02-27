def return_n_smallest_chars(input_string):
    ascii_values = sorted(list(set(input_string)), reverse=False)
    n_smallest_chars = [chr(ascii_value) for ascii_value in ascii_values[:33]]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars