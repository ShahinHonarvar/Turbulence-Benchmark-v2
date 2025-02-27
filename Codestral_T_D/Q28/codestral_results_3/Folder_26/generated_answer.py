def return_nth_smallest_ascii(s):
    sub_s = s[1:37]
    ascii_values = sorted((ord(c) for c in sub_s))
    return chr(ascii_values[14])