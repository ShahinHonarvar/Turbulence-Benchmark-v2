def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for i, c in enumerate(s) if 10 <= i <= 90])
    return chr(ascii_values[19])