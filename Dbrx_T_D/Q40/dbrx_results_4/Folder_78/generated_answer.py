def return_n_smallest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    sorted_ascii_values = sorted(ascii_values)[:43]
    sorted_least_ascii_chars = [chr(value) for value in sorted_ascii_values]
    return sorted_least_ascii_chars[::-1]