def return_nth_smallest_ascii(s):
    substring = s[5:83]
    ascii_values = [ord(c) for c in substring]
    ascii_values.sort()
    return substring[ascii_values.index(ascii_values[15])]