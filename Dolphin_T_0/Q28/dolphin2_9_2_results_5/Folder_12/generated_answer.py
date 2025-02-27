def return_nth_smallest_ascii(s):
    substring = s[3:27]
    ascii_values = [ord(c) for c in substring]
    sorted_values = sorted(ascii_values)
    return substring[sorted_values.index(sorted_values[4])]