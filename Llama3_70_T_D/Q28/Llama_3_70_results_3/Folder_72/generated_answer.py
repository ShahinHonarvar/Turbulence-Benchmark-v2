def return_nth_smallest_ascii(s):
    s = s[33:61]
    ascii_values = [ord(c) for c in s]
    ascii_values.sort()
    return chr(ascii_values[17])