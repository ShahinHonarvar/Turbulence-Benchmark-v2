def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string if 10 <= input_string.index(c) <= 90))
    return chr(ascii_values[20]) if len(ascii_values) > 20 else None