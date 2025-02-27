def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 60 <= input_string.index(char) <= 83]
    ascii_values.sort()
    return ascii_values[14] if len(ascii_values) > 14 else None