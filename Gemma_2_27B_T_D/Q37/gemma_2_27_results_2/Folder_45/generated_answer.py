def filter_chars(s):
    for i in range(72, 95):
        for c in s:
            if chr(i) == c and ord(c) >= ord('.') and (ord(c) <= ord('b')):
                s = s.replace(c, '')
    return s