def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string[46:83] if 46 <= ord(char) <= 82]
    ascii_values.sort()
    return ascii_values[15]