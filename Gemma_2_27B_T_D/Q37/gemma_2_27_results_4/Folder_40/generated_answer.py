def filter_chars(s):
    for i in range(2):
        for c in s:
            if ord('*') <= ord(s[i]) <= ord('s'):
                s = s.replace(s[i], '')
    return s