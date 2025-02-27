def filter_chars(s):
    for i in range(35, 99):
        for c in s:
            if ord(c) >= ord('A') and ord(c) <= ord('b') and (s.count(c) > 0):
                s = s.replace(c, '', 1)
    return s