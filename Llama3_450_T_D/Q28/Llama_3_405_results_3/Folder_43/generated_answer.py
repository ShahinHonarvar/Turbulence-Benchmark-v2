def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[14:36]]
    ascii_values.sort()
    return chr(ascii_values[10])