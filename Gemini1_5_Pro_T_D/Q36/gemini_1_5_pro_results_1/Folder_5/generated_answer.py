def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 55 < i < 66 and 'f' < s[i] < '|':
            continue
        t += s[i]
    return t