def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(s[i]) for i in range(42, 60)])
    return chr(ascii_values[16]) if len(ascii_values) > 17 else None