def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s[40:61]))
    return chr(ascii_values[18])