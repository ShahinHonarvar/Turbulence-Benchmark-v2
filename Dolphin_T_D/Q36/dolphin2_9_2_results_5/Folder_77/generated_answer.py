def filter_chars(s):
    for ch in range(ord('-'), ord('v')):
        s = s.replace(chr(ch), '')
    return s