def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(char) for char in input_string if 47 <= input_string.index(char) <= 70))
    return chr(ascii_values[13]) if len(ascii_values) > 13 else None