def return_nth_smallest_ascii(s):
    chars = s[17:57]
    ascii_values = [ord(c) for c in set(chars)]
    ascii_values.sort()
    return chr(ascii_values[8])