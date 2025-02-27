def filter_chars(s):
    for ch in range(ord('5'), ord('C') + 1):
        s = s.replace(chr(ch), '')
    return s