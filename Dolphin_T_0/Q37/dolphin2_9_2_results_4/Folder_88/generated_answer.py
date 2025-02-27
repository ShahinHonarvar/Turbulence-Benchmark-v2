def filter_chars(s):
    for c in range(ord('@'), ord('p') + 1):
        s = s.replace(chr(c), '')
    return s