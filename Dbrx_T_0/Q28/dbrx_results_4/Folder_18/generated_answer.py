def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string[51:61] if char in input_string[51:61]]
    ascii_values.sort()
    return chr(ascii_values[4])