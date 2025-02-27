def filter_chars(s):
    for c in range(ord('&'), ord('M')):
        if chr(c) in s[46:74]:
            s = s.replace(chr(c), '')
    return s