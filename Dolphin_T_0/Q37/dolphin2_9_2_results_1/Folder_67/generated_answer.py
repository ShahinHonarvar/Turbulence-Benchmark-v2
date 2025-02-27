def filter_chars(s):
    for ch in range(ord(']'), ord('t') + 1):
        s = s.replace(chr(ch), '')
    return s