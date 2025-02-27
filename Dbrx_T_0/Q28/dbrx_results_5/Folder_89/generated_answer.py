def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 24 <= input_string.index(char) <= 71]
    ascii_values.sort()
    return chr(ascii_values[7]) if len(ascii_values) > 7 else None