def return_nth_smallest_ascii(input_string):
    substring = input_string[5:83]
    ascii_values = [ord(char) for char in substring]
    ascii_values.sort()
    return chr(ascii_values[15])