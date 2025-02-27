def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 23 < i < 83 and 'f' < s[i] < 'o':
            continue
        t += s[i]
    return t