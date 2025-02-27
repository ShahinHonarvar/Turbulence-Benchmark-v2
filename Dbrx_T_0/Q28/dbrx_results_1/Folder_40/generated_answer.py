def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 0 <= input_string.index(char) <= 4]
    ascii_values.sort()
    return chr(ascii_values[4])