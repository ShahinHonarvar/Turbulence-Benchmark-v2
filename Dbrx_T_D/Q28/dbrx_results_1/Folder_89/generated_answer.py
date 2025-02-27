def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string if 24 <= input_string.index(c) <= 71))
    return chr(ascii_values[7]) if len(ascii_values) > 7 else None