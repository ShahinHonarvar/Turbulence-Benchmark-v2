def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if 12 <= s.index(c) <= 72))
    return chr(ascii_values[12])