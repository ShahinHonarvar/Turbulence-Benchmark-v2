def return_nth_smallest_ascii(string):
    ascii_values = sorted([ord(char) for char in string[42:60]])
    return chr(ascii_values[16])