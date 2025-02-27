def return_nth_smallest_ascii(s):
    sub_str = s[67:78]
    ascii_values = [ord(c) for c in sub_str]
    ascii_values.sort()
    return chr(ascii_values[6])