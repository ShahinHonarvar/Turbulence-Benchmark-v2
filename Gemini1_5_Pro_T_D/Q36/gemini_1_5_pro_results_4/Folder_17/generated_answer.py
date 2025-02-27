def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 18 and i < 95 and (s[i] > 'K') and (s[i] < 'a'):
            continue
        else:
            t += s[i]
    return t