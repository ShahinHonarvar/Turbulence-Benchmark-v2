def return_nth_smallest_ascii(s):
    chars = sorted(s[12:56])
    ascii_values = sorted([ord(char) for char in chars])
    return chr(ascii_values[16])