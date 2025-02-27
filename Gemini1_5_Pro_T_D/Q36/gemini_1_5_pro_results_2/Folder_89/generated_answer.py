def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 57 and i < 69 and (s[i] > '(') and (s[i] < 'W'):
            t = t
        else:
            t += s[i]
    return t