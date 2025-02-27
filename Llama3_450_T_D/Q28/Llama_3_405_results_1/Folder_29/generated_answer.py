def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for i, c in enumerate(s) if 5 <= i <= 10])
    return chr(ascii_values[5])