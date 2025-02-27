def return_nth_smallest_ascii(s):
    substring = s[3:53]
    ascii_values = sorted(map(ord, substring))
    return chr(ascii_values[7])