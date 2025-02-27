def filter_chars(s):
    for i in range(34, 68):
        if ord(s[i]) >= ord('W') and ord(s[i]) <= ord('x'):
            s = s.replace(s[i], '')
    return s