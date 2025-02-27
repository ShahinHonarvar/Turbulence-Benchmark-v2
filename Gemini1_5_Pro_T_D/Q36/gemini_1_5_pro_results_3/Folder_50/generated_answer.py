def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if 61 < i < 88 and '%' < c < 'q':
            continue
        t += c
    return t