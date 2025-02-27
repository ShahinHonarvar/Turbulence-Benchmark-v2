def return_nth_smallest_ascii(s):
    chars = s[58:86]
    ascii_values = [ord(c) for c in chars]
    sorted_ascii = sorted(ascii_values)
    return chr(sorted_ascii[18])