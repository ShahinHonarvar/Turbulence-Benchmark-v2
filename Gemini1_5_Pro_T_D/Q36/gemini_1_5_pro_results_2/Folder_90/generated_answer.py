def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 344 and i < 874 and (s[i] > 'f') and (s[i] < '~'):
            t = t + ''
        else:
            t = t + s[i]
    return t