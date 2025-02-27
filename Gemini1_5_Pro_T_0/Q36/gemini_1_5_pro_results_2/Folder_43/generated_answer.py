def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 27 and i < 75 and (s[i] > 'A') and (s[i] < 'i'):
            continue
        else:
            t += s[i]
    return t