def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 58 <= ord(char) <= 85]
    ascii_values.sort()
    return chr(ascii_values[18]) if len(ascii_values) > 18 else None