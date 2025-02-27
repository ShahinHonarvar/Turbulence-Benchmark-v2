def return_nth_smallest_ascii(s):
    chars = sorted(s[8:27])
    ascii_vals = sorted([ord(char) for char in chars])
    return chr(ascii_vals[5])