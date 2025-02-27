def return_nth_smallest_ascii(string):
    ascii_values = sorted((ord(c) for c in string if 0 <= string.index(c) <= 3))
    return chr(ascii_values[4]) if len(ascii_values) > 4 else None