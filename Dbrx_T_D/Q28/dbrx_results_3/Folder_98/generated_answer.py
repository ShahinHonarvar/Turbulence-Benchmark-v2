def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 0 <= s.index(c) <= 8]
    ascii_values.sort()
    return chr(ascii_values[8])