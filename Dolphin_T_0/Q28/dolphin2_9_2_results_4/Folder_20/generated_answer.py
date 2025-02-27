def return_nth_smallest_ascii(s):
    subset = s[25:65]
    ascii_values = [ord(c) for c in subset]
    ascii_values.sort()
    return chr(ascii_values[5])