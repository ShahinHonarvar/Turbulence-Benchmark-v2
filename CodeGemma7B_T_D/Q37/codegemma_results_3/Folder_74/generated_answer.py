def filter_chars(s):
    for i in range(19, 33):
        for c in s:
            if c == chr(i):
                s = s.replace(c, '')
    return s