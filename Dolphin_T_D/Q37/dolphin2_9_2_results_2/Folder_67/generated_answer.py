def filter_chars(s):
    for c in range(ord('['), ord('t') + 1):
        for i in range(19, 23):
            s = s[:i] + s[i:].replace(chr(c), '')
    return s