def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s[13:36]))
    return chr(ascii_values[17]) if len(ascii_values) > 17 else None