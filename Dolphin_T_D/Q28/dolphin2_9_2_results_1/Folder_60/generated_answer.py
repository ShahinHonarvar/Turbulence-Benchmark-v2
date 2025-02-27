def return_nth_smallest_ascii(string):
    chars = list(string[36:80])
    ascii_values = [ord(c) for c in chars]
    ascii_values.sort()
    return chars[ascii_values.index(ascii_values[11])]