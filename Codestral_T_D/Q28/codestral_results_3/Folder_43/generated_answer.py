def return_nth_smallest_ascii(s):
    sub_s = s[14:36]
    ascii_values = sorted(map(ord, sub_s))
    return chr(ascii_values[10])