def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(c) for c in s[60:84]])
    return chr(ascii_values[13])