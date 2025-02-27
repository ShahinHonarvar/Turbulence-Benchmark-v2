def return_nth_smallest_ascii(s):
    substring = s[22:75]
    ascii_values = sorted(map(ord, substring))
    return chr(ascii_values[11])