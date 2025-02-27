def return_nth_smallest_ascii(s):
    chars = s[17:66]
    ascii_chars = [(ord(c), c) for c in chars]
    ascii_chars.sort()
    return ascii_chars[7][1]