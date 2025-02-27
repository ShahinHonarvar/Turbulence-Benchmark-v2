def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if 163 < i < 658 and '(' < c < ']':
            t = t.replace(c, '')
        else:
            t += c
    return t