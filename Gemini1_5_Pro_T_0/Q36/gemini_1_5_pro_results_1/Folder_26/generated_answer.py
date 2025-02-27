def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if 43 < i < 83 and ':' < c < 'Q':
            continue
        t += c
    return t