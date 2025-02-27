def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 57 < i < 69 and '(' < s[i] < 'W':
            continue
        t += s[i]
    return t