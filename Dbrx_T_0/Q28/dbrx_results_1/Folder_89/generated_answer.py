def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 24 <= s.index(c) <= 71]
    ascii_values.sort()
    return chr(ascii_values[7])