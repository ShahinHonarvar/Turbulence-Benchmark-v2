def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(char) for char in set(input_string)))
    return chr(ascii_values[17])