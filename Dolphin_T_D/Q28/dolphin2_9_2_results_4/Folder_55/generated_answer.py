def return_nth_smallest_ascii(s):
    chars = list(s)
    char_values = [ord(c) for c in chars[:13]]
    char_values.sort()
    return chr(char_values[12])