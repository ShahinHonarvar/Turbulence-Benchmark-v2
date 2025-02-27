def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 17 <= s.index(c) <= 65]
    ascii_values.sort()
    return chr(ascii_values[7]) if len(ascii_values) > 7 else None