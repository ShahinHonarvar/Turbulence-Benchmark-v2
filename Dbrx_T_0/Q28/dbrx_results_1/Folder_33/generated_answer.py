def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 22 <= s.index(c) <= 74]
    ascii_values.sort()
    return chr(ascii_values[11]) if len(ascii_values) > 12 else None