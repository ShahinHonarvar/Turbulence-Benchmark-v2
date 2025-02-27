def return_nth_smallest_ascii(s):
    substr = s[38:65]
    ascii_values = [ord(c) for c in substr]
    ascii_values.sort()
    return chr(ascii_values[13])