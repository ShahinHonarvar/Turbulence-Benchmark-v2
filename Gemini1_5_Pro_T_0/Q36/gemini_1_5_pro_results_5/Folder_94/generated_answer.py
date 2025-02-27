def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 15 and i < 85 and (s[i] > 'I') and (s[i] < 'M'):
            continue
        else:
            t += s[i]
    return t