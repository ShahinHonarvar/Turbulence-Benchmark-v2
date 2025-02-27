def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string[51:90] if 51 <= input_string.index(c) <= 89))
    return chr(ascii_values[13]) if len(ascii_values) > 13 else None