def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 9 <= s.index(c) <= 59]
    ascii_values.sort()
    return chr(ascii_values[5])