def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string[17:84] if char != ' ']
    ascii_values.sort()
    return ascii_values[4]