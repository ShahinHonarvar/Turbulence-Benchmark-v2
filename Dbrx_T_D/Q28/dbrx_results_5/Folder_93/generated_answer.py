def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 42 <= input_string.index(char) <= 59]
    ascii_values.sort()
    return chr(ascii_values[16])