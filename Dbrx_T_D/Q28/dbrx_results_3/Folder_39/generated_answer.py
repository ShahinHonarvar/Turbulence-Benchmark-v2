def return_nth_smallest_ascii(s):
    ascii_chars = [ord(c) for c in s if 0 < s.index(c) <= 66]
    ascii_chars.sort()
    return chr(ascii_chars[7])