def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 0 <= s.index(c) <= 6]
    ascii_values.sort()
    return chr(ascii_values[6]) if len(ascii_values) > 6 else None