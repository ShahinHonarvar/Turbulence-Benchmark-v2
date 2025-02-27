def return_n_smallest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    ascii_values.sort()
    n_smallest_ascii_values = ascii_values[:21]
    n_smallest_chars = [chr(value) for value in n_smallest_ascii_values]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars