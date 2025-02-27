def return_nth_smallest_ascii(s):
    chars = sorted(s[34:82])
    ascii_values = sorted([ord(char) for char in chars])
    return chr(ascii_values[11])