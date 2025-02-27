def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 43 and i < 69 and (s[i] > 'B') and (s[i] < 'r'):
            t = t + ''
        else:
            t = t + s[i]
    return t