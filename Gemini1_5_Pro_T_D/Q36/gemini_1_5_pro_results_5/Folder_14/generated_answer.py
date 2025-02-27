def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 41 and i < 56 and (s[i] > 'Z') and (s[i] < 'c'):
            continue
        else:
            t += s[i]
    return t