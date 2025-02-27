def return_nth_smallest_ascii(s):
    sub_str = s[9:23]
    ascii_values = sorted([ord(c) for c in sub_str])
    return chr(ascii_values[3])