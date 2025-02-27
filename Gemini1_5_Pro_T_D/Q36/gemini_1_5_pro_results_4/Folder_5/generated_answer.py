def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 55 and i < 66 and (s[i] > 'f') and (s[i] < '|'):
            continue
        else:
            t += s[i]
    return t