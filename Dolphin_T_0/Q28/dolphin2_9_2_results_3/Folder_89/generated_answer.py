def return_nth_smallest_ascii(s):
    chars = s[24:72]
    ascii_values = [ord(c) for c in chars]
    ascii_values.sort()
    return chr(ascii_values[7])