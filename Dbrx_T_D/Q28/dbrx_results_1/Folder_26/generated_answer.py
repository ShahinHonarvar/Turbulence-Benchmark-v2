def return_nth_smallest_ascii(string):
    ascii_values = sorted((ord(c) for c in string if 1 <= string.index(c) <= 36))
    return chr(ascii_values[14]) if len(ascii_values) > 14 else None