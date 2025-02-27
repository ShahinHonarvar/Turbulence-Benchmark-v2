def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 171 and i < 636 and (s[i] > 'c') and (s[i] < 's'):
            continue
        else:
            t += s[i]
    return t