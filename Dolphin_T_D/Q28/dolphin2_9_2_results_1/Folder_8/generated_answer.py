def return_nth_smallest_ascii(s):
    narrowed_s = s[60:89]
    ascii_vals = {char: ord(char) for char in narrowed_s}
    sorted_chars = sorted(ascii_vals, key=ascii_vals.get)
    return sorted_chars[6]