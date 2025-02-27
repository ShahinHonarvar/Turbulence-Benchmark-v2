def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 23 and i < 83 and (s[i] > 'f') and (s[i] < 'o'):
            continue
        else:
            t += s[i]
    return t