def filter_chars(s):
    for c in [chr(i) for i in range(ord(';'), ord('b') + 1)]:
        if c in s[27:30]:
            s = s.replace(c, '')
    return s