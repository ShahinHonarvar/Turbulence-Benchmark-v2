def return_nth_smallest_ascii(s):
    chars = sorted(s[1:67])
    ascii_values = sorted([ord(c) for c in chars])
    return chr(ascii_values[7])