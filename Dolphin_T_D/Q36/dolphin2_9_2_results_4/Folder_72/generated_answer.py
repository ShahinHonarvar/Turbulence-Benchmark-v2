def filter_chars(s):
    for ch in range(ord('W') + 1, ord('x')):
        s = s.replace(chr(ch), '')
    return s