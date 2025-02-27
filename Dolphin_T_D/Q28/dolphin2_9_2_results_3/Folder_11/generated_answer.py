def return_nth_smallest_ascii(s):
    chars = s[9:60]
    ascii_values = sorted([ord(c) for c in chars])
    return chr(ascii_values[5])