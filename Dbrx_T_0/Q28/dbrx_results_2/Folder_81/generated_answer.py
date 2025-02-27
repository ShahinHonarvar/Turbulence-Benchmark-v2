def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if s.index(c) <= 13))[:14]
    return chr(ascii_values[13])