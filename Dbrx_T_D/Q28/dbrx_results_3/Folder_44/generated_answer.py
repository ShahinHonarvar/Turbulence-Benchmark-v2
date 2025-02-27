def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string[20:31] if char in input_string[20:31]]
    ascii_values.sort()
    return ascii_values[7] if len(ascii_values) > 7 else None