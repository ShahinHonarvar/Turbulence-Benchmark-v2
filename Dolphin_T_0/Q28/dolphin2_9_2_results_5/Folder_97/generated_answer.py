def return_nth_smallest_ascii(s):
    subset = s[15:22]
    ascii_values = [ord(c) for c in subset]
    ascii_values.sort()
    return subset[ascii_values.index(ascii_values[5])]