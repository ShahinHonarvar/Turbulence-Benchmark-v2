def return_n_smallest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    smallest_chars = [char for char, ascii in zip(input_string, ascii_values) if ascii in sorted(ascii_values)[:70]]
    smallest_chars.sort(key=ord, reverse=True)
    return smallest_chars