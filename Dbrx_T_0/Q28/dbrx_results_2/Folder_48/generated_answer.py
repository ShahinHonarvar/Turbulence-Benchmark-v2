def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 37 <= s.index(c) <= 59]
    ascii_values.sort()
    return chr(ascii_values[5]) if len(ascii_values) >= 6 else None