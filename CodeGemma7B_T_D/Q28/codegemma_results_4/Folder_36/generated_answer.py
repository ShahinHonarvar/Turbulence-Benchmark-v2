def return_nth_smallest_ascii(string):
    ascii_values = sorted([ord(char) for char in string if 16 < string.index(char) <= 56])
    return chr(ascii_values[8])