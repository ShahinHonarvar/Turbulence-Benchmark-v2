def filter_chars(s):
    for i in range(19, 23):
        if i < len(s):
            c = s[i]
            if ord(c) >= ord(']') and ord(c) <= ord('t'):
                s = s.replace(c, '')
    return s