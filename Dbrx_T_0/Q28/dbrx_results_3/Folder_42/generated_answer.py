def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string if 12 <= input_string.index(c) <= 72))
    return chr(ascii_values[12]) if len(ascii_values) > 12 else None