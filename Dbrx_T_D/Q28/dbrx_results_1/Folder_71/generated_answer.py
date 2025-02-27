def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string if 5 <= input_string.index(c) <= 82))
    return chr(ascii_values[15]) if len(ascii_values) > 15 else None