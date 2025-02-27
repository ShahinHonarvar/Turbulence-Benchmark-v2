def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if 44 <= s.index(c) <= 69]
    ascii_values.sort()
    return chr(ascii_values[14])