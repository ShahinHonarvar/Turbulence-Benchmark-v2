def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 10 <= input_string.index(char) <= 90]
    ascii_values.sort()
    return chr(ascii_values[19])