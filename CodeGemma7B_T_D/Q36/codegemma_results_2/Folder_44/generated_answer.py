def filter_chars(s):
    for i in range(18, 64):
        if ord(s[i]) > ord('3') and ord(s[i]) < ord('B'):
            s = s.replace(s[i], '')
    return s