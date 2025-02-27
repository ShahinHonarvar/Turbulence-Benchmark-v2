def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if input_string.index(char) >= 28 and input_string.index(char) <= 67]
    ascii_values.sort()
    return chr(ascii_values[14])