def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if i > 42 and i < 67 and (s[i] > '6') and (s[i] < 'g'):
            continue
        else:
            t += s[i]
    return t