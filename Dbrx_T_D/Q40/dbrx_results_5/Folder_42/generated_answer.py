def return_n_smallest_chars(input_string):
    ascii_values = sorted((ord(c) for c in input_string))
    n_smallest_ascii_values = ascii_values[:59]
    n_smallest_chars = [chr(c) for c in n_smallest_ascii_values]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars