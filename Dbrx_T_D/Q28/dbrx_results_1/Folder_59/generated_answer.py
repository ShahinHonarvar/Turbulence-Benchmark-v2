def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in set(input_string) if 0 <= input_string.index(c) <= 11))
    return chr(ascii_values[11]) if len(ascii_values) >= 12 else None