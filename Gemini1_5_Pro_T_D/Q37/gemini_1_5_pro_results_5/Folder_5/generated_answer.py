def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if i >= 24 and i <= 82 and (c >= '5') and (c <= '<'):
            t = t.replace(c, '')
        else:
            t += c
    return t