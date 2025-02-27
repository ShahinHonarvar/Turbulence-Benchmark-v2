def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 32 <= ord(c) <= 67]
    ascii_values.sort()
    return chr(ascii_values[11]) if len(ascii_values) > 11 else None