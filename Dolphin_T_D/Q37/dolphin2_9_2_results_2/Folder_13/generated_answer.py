def filter_chars(s):
    for i in range(124, 855):
        if i >= 9 and i <= s:
            s = s.replace(chr(i), '')
    return s