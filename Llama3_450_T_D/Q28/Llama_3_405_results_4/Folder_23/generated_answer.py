def return_nth_smallest_ascii(s):
    sliced_s = s[29:48]
    ascii_values = [ord(c) for c in sliced_s]
    ascii_values.sort()
    return chr(ascii_values[6])