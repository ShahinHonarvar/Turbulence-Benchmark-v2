def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(1, 47)]
    ascii_values = [ord(c) for c in chars]
    ascii_values.sort()
    return chars[ascii_values.index(ascii_values[12])]