def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 40 <= s.index(c) <= 60]
    ascii_values.sort()
    return chr(ascii_values[18]) if len(ascii_values) > 18 else None