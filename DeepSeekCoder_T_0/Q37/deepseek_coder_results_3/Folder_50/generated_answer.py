def filter_chars(s):
    for i in range(71, 97):
        if ord('_') <= ord(s[i]) <= ord('o'):
            s = s.replace(s[i], '')
    return s