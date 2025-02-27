def filter_chars(s):
    for i in range(54, 63):
        if i < len(s):
            c = s[i]
            if ord(c) >= ord(')') and ord(c) <= ord('9'):
                s = s.replace(c, '')
    return s