def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 33 <= ord(char) <= 85]
    ascii_values.sort()
    return ascii_values[12]