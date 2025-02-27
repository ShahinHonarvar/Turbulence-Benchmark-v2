def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string[18:46]))
    return chr(ascii_values[6]) if len(ascii_values) > 6 else None