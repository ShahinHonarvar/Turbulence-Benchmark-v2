def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 17 <= input_string.index(char) <= 65]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[7])