def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 35 <= input_string.index(char) <= 52]
    ascii_values.sort()
    return chr(ascii_values[9]) if len(ascii_values) > 9 else None