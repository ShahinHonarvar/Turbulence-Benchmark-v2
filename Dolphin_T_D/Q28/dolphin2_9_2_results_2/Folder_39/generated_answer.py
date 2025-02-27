def return_nth_smallest_ascii(s):
    chars = [c for c in s[1:67]]
    ascii_chars = [(ord(c), c) for c in chars]
    ascii_chars.sort()
    return ascii_chars[7][1]