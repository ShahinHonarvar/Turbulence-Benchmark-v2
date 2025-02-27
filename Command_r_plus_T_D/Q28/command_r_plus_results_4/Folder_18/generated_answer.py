def return_nth_smallest_ascii(s):
    sub_s = s[51:61]
    ascii_values = [ord(c) for c in sub_s]
    ascii_values.sort()
    return chr(ascii_values[4])