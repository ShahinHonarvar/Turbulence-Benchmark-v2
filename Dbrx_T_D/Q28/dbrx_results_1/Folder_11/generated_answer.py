def return_nth_smallest_ascii(s):
    ascii_vals = sorted((ord(c) for c in s[9:60] if c.isalnum()))
    return chr(ascii_vals[5]) if len(ascii_vals) > 5 else None