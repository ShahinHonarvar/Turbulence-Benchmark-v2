def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 43 < i < 83 and ':' < s[i] < 'Q':
            continue
        else:
            t += s[i]
    return t