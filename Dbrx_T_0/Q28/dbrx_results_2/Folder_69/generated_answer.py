def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 67 <= input_string.index(char) <= 77]
    ascii_values.sort()
    return chr(ascii_values[6]) if len(ascii_values) >= 7 else None