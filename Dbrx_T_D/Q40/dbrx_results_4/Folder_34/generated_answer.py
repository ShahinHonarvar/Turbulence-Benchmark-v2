def return_n_smallest_chars(input_str):
    ascii_values = [ord(char) for char in input_str]
    sorted_ascii_values = sorted(ascii_values)[:9]
    sorted_chars = [chr(ascii) for ascii in sorted_ascii_values]
    return sorted_chars[::-1]