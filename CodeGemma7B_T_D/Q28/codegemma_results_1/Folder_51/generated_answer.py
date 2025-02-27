def return_nth_smallest_ascii(string):
    ascii_values = sorted([ord(char) for char in string[10:74]])
    return chr(ascii_values[8])