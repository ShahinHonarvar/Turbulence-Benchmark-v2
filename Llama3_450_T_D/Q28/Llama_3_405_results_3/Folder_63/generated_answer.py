def return_nth_smallest_ascii(s):
    section = s[47:71]
    ascii_values = sorted([ord(c) for c in section])
    return chr(ascii_values[13])