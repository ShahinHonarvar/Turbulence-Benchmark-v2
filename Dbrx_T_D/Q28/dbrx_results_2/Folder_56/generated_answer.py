def return_nth_smallest_ascii(s):
    sub_s = s[0:5]
    ascii_values = [ord(c) for c in sub_s]
    ascii_values.sort()
    return sub_s[sub_s.index(chr(ascii_values[3]))]