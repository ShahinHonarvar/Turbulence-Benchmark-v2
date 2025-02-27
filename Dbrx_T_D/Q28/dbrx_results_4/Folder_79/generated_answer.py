def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(c) for c in input_string if 13 <= input_string.index(c) <= 35]
    return chr(sorted(ascii_values)[17]) if len(ascii_values) > 18 else None