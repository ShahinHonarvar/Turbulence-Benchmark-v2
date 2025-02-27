def filter_chars(s):
    for c in [chr(i) for i in range(ord('W'), ord('[') + 1)]:
        s = s.replace(c, '')
    return s