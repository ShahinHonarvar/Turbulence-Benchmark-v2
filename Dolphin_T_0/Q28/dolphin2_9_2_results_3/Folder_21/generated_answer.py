def return_nth_smallest_ascii(s):
    chars = s[8:66]
    ascii_values = [ord(c) for c in chars]
    ascii_values.sort()
    return chars[ascii_values.index(ascii_values[5])]