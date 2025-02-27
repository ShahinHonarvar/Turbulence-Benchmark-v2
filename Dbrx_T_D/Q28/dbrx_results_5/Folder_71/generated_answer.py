def return_nth_smallest_ascii(input_str):
    ascii_values = [ord(char) for char in input_str[5:83] if input_str.index(char) == input_str[5:83].index(char)]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[15])