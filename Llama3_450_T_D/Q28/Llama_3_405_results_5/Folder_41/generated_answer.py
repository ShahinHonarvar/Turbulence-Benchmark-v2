def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for i, c in enumerate(s) if 58 <= i <= 85])
    return chr(ascii_values[18])