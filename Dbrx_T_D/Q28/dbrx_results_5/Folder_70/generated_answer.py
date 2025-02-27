def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 28 <= s.index(c) <= 54]
    ascii_values.sort()
    return chr(ascii_values[13])