def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 10 < i < 79 and '?' < s[i] < 'm':
            t = t.replace(s[i], '')
        else:
            t += s[i]
    return t