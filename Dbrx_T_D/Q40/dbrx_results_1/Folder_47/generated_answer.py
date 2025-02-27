def return_n_smallest_chars(input_string):
    ascii_values_list = [ord(char) for char in input_string]
    n_smallest_ascii_values = sorted(ascii_values_list)[:21]
    n_smallest_chars = [chr(ascii_value) for ascii_value in sorted(n_smallest_ascii_values, reverse=True)]
    return n_smallest_chars