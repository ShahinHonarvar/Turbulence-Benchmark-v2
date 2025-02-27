def return_nth_smallest_ascii(s):
    substring = s[34:82]
    ascii_values = list(map(ord, substring))
    ascii_values.sort()
    return substring[ascii_values.index(ascii_values[11])]