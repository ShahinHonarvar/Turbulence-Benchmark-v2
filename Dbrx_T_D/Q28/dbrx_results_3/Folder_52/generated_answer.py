def return_nth_smallest_ascii(input_str):
    ascii_values = [ord(char) for char in input_str if 46 <= input_str.index(char) <= 72]
    ascii_values.sort()
    return ascii_values[14]