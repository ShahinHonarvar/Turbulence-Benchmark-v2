def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 23 and i < 45 and (s[i] > '3') and (s[i] < 'I'):
            continue
        t += s[i]
    return t