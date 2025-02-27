def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 29 <= input_string.index(char) <= 47]
    ascii_values.sort()
    return ascii_values[6] if len(ascii_values) >= 7 else None