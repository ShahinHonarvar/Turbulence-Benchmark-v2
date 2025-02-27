def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 24 and i < 37 and (s[i] > 'A') and (s[i] < 'h'):
            t = t
        else:
            t = t + s[i]
    return t