def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(c) for c in input_string if 10 <= input_string.index(c) <= 82]
    ascii_values.sort()
    return chr(ascii_values[17]) if len(ascii_values) > 17 else None