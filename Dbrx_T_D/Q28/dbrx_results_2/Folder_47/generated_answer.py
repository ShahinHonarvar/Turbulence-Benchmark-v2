def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in set(s[3:53])))
    return chr(ascii_values[7]) if len(ascii_values) > 7 else None