def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if 10 <= s.index(c) <= 73))
    return chr(ascii_values[9]) if len(ascii_values) > 9 else None