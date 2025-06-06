def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 34 <= s.index(c) <= 81]
    ascii_values.sort()
    return chr(ascii_values[11]) if len(ascii_values) > 12 else None