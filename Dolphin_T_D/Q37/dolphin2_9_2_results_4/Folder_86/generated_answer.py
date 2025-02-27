def filter_chars(s):
    for c in s:
        if ord(c) >= ord('O') and ord(c) <= ord('}'):
            s = s.replace(c, '')
    return s