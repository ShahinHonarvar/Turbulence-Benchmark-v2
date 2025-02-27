def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 34 <= s.index(c) <= 85]
    ascii_values.sort()
    return chr(ascii_values[19]) if len(ascii_values) >= 20 else None