def filter_chars(s):
    for ch in range(ord('?'), ord('m')):
        s = s.replace(chr(ch), '')
    return s