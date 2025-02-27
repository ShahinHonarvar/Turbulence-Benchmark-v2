def filter_chars(s):
    for i in range(23, 90):
        c = s[i]
        if ord(c) >= ord('w') and ord(c) <= ord('{'):
            s = s.replace(c, '')
    return s