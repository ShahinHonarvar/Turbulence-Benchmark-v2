def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 171 < i < 636 and 'c' < s[i] < 's':
            continue
        t += s[i]
    return t