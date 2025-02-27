def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if 3 <= s.index(c) <= 26))
    return chr(ascii_values[4]) if len(ascii_values) >= 5 else None