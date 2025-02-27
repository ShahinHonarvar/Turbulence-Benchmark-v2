def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if 0 <= s.index(c) <= 87))
    return chr(ascii_values[13]) if len(ascii_values) > 13 else None