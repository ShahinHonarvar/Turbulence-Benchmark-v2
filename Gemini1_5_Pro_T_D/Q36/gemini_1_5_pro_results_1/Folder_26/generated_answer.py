def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 43 and i < 83 and (s[i] > ':') and (s[i] < 'Q'):
            t = t + ''
        else:
            t = t + s[i]
    return t