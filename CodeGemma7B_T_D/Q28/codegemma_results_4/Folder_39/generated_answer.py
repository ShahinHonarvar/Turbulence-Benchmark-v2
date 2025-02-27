def return_nth_smallest_ascii(char):
    ascii_values = sorted([ord(c) for c in char[1:67]])
    return chr(ascii_values[7])