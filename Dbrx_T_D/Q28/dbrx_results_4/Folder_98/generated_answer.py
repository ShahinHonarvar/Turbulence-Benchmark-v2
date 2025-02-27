def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if input_string.index(char) in range(9)]
    ascii_values.sort()
    return chr(ascii_values[8]) if len(ascii_values) > 8 else None