def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 4 <= input_string.index(char) <= 33]
    ascii_values.sort()
    return ascii_values[3] if len(ascii_values) > 3 else None