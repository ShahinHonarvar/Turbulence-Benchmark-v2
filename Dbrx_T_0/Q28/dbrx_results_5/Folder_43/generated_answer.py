def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string[14:36]))
    return chr(ascii_values[10]) if len(ascii_values) > 10 else None