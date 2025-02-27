def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 56 and i < 86 and (s[i] > '+') and (s[i] < 'w'):
            continue
        else:
            t += s[i]
    return t