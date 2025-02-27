def return_nth_smallest_ascii(s):
    substring = s[38:83]
    ascii_values = [ord(c) for c in substring]
    sorted_values = sorted(ascii_values)
    return substring[ascii_values.index(sorted_values[19])]