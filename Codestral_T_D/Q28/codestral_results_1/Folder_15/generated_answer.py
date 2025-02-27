def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for c in s[0:6]])
    return chr(ascii_values[5])