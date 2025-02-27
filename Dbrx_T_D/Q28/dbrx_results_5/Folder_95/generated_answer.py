def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(char) for char in input_string if 1 <= input_string.index(char) <= 46))
    return chr(ascii_values[12])