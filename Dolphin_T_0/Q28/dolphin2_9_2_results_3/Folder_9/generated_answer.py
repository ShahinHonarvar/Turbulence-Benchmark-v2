def return_nth_smallest_ascii(s):
    chars = s[10:91]
    ascii_values = list(map(ord, chars))
    ascii_values.sort()
    return chr(ascii_values[19])