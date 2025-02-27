def return_n_smallest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    ascii_values.sort()
    n_smallest_chars = [char for char in ascii_values[:45]]
    return n_smallest_chars