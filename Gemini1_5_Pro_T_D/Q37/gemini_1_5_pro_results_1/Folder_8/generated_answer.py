def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i >= 41 and i <= 86 and (s[i] >= 'S') and (s[i] <= 's'):
            continue
        else:
            t += s[i]
    return t