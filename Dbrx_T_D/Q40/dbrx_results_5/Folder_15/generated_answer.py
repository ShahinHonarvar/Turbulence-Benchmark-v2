def return_n_smallest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    ascii_values.sort()
    n_smallest_ascii = ascii_values[:57]
    n_smallest_chars = [chr(ascii) for ascii in n_smallest_ascii]
    return n_smallest_chars