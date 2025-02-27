def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(x) for i, x in enumerate(s[:7])])
    return chr(ascii_values[6])