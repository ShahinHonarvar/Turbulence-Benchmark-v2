def return_nth_smallest_ascii(s):
    substring = s[35:52]
    ascii_values = [ord(i) for i in substring]
    ascii_values.sort()
    return substring[ascii_values.index(ascii_values[9])]