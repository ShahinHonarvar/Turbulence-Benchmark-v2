def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 33 <= ord(c) <= 60]
    ascii_values.sort()
    return chr(ascii_values[17]) if len(ascii_values) > 17 else None