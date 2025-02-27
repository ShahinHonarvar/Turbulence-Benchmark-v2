def return_nth_smallest_ascii(input_str):
    ascii_values = [ord(c) for c in set(input_str[8:66])]
    ascii_values.sort()
    return chr(ascii_values[5])