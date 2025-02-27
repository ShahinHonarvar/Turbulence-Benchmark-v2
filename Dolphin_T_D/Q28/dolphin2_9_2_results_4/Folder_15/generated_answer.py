def return_nth_smallest_ascii(s):
    chars = list(s)
    chars.sort()
    ascii_values = [ord(c) for c in chars]
    return chars[ascii_values.index(sorted(ascii_values)[5])]