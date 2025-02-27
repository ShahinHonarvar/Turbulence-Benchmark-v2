def return_nth_smallest_ascii(s):
    sub_s = s[28:55]
    ascii_values = sorted((ord(c) for c in set(sub_s)))
    return chr(ascii_values[13])