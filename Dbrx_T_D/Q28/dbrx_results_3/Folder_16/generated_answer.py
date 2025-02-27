def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(c) for c in input_string[18:46]]
    ascii_values.sort()
    return chr(ascii_values[6])