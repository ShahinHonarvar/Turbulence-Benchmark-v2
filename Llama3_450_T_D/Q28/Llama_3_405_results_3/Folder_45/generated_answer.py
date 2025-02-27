def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for i, c in enumerate(s[:16])])
    return chr(ascii_values[15])