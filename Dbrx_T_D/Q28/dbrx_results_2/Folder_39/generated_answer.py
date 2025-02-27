def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(c) for c in input_string if 1 <= input_string.index(c) <= 66]
    ascii_values.sort()
    return chr(ascii_values[7])