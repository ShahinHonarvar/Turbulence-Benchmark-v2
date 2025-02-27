def return_nth_smallest_ascii(s):
    chars = sorted(s[1:47])
    ascii_values = sorted([ord(char) for char in chars])
    return chr(ascii_values[12])