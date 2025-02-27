def return_nth_smallest_ascii(s):
    sub_s = s[40:61]
    ascii_values = sorted((ord(c) for c in sub_s))
    return chr(ascii_values[18])