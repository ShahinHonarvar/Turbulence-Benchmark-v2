def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in s[25:78] if 0 < ord(c) < 128]
    ascii_chars.sort()
    return chr(ascii_chars[15])