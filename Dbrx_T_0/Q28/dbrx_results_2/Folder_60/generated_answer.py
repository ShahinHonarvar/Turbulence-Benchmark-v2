def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 36 <= s.index(c) <= 79]
    ascii_values.sort()
    return chr(ascii_values[11]) if len(ascii_values) > 11 else None