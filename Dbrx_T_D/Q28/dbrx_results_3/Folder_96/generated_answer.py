def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(char) for char in input_string if 0 <= input_string.index(char) <= 17]
    sorted_ascii_values = sorted(ascii_values)[:18]
    return chr(sorted_ascii_values[17])