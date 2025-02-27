def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 48 <= ord(char) <= 76]
    ascii_values.sort()
    return chr(ascii_values[5]) if len(ascii_values) > 5 else None