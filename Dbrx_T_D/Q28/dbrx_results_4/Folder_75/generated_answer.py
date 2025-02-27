def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 62 <= s.index(c) <= 83]
    ascii_values.sort()
    return chr(ascii_values[9])