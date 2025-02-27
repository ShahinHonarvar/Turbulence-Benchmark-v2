def filter_chars(s):
    for i in range(57, 69):
        while i in s:
            s = s.replace(chr(i), '', 1)
    return s