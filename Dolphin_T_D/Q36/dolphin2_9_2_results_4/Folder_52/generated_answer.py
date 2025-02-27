def filter_chars(s):
    for c in range(ord('A'), ord('Z') + 1):
        if ord('I') < c < ord('a'):
            s = s.replace(chr(c), '')
    return s