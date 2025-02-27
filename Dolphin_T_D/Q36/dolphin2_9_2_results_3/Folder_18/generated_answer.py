def filter_chars(s):
    for i in range(587, 648):
        if ord(s[i]) > ord(',') and ord(s[i]) < ord('c'):
            s = s.replace(s[i], '')
    return s