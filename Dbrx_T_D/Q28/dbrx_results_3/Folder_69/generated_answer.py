def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(c) for c in input_string[67:78] if c != ' ']
    ascii_values.sort()
    return ascii_values[7]