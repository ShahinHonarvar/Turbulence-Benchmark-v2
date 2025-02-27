def filter_chars(s):
    for i in range(24, 83):
        c = s[i]
        if c.ord() >= ord('5') and c.ord() <= ord('<'):
            s = s.replace(c, '')
    return s