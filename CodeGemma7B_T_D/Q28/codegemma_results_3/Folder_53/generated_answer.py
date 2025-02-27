def return_nth_smallest_ascii(string):
    ascii_values = sorted([ord(c) for c in string if 40 <= string.index(c) <= 60])
    return chr(ascii_values[18])