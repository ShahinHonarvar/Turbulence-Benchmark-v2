def filter_chars(s):
    for c in [chr(i) for i in range(ord('w'), ord('{') + 1)]:
        s = s.replace(c, '')
    return s