def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 10 <= s.index(c) <= 90]
    ascii_values.sort()
    return chr(ascii_values[19]) if len(ascii_values) > 19 else None