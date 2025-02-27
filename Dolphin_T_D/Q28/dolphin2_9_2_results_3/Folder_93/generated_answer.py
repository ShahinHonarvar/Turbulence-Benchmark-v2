def return_nth_smallest_ascii(input_string):
    substring = input_string[42:60]
    ascii_values = [ord(c) for c in substring]
    ascii_values.sort()
    return chr(ascii_values[16])