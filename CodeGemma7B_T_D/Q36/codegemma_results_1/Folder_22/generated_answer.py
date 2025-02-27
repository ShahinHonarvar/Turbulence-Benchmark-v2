def filter_chars(s):
    for i in range(55, 84):
        if ord(s[i]) > ord(';') and ord(s[i]) < ord('z'):
            while s.count(s[i]) > 0:
                s = s[:i] + s[i + 1:]
    return s