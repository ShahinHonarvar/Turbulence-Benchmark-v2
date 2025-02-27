def return_nth_smallest_ascii(s):
    substring = s[5:90]
    ascii_values = sorted([ord(c) for c in set(substring)])
    return chr(ascii_values[12])