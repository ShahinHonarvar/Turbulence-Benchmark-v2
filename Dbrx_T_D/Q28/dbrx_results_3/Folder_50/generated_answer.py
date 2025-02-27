def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 25 <= s.index(c) <= 88]
    ascii_values.sort()
    return chr(ascii_values[10]) if len(ascii_values) > 10 else None