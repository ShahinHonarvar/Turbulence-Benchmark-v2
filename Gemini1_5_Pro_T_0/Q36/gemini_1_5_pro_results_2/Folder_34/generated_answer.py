def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 10 and i < 79 and (s[i] > '?') and (s[i] < 'm'):
            t = t + ''
        else:
            t = t + s[i]
    return t