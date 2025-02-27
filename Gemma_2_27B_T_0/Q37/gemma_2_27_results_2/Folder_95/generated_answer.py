def filter_chars(s):
    for i in range(35, 41):
        if i < len(s):
            c = s[i]
            if ord(c) >= ord(')') and ord(c) <= ord('l'):
                s = s.replace(c, '')
    return s