def filter_chars(s):
    for c in range(ord(s[0]), ord(s[1]) + 1):
        s = s.replace(chr(c), '')
    return s