def return_nth_smallest_ascii(s):
    substring = s[58:86]
    ascii_values = [ord(c) for c in substring]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[18])