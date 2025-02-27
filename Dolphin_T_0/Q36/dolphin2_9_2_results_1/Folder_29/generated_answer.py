def filter_chars(s):
    for c in range(ord('H'), ord('s')):
        if chr(c) in s[46:68]:
            s = s.replace(chr(c), '')
    return s