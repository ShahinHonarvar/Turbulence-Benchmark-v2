def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s[17:57] if c.isalnum()))
    return chr(ascii_values[8]) if len(ascii_values) > 8 else None