def return_n_smallest_chars(input_str):
    ascii_values = [ord(char) for char in input_str]
    ascii_values.sort()
    n_smallest_ascii_values = ascii_values[:29]
    n_smallest_chars = [chr(ascii) for ascii in n_smallest_ascii_values]
    return n_smallest_chars