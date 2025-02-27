def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 51 and i < 76 and (s[i] > '5') and (s[i] < 'f'):
            continue
        else:
            t += s[i]
    return t