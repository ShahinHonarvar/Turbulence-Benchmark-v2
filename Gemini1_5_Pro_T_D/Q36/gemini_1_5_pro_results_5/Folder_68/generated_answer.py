def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 1 and i < 9 and (s[i] > '8') and (s[i] < 'm'):
            continue
        else:
            t += s[i]
    return t