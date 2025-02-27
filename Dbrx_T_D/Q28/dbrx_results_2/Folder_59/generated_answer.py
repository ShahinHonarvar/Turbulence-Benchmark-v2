def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in set(input_string) if input_string.index(c) in range(12)))
    return chr(ascii_values[11]) if len(ascii_values) > 11 else None