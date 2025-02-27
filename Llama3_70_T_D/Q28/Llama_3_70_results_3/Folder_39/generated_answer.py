def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for c in s[1:67]])
    return chr(ascii_values[7])