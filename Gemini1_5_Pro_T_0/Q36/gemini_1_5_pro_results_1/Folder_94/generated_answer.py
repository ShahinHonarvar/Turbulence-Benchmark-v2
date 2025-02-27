def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 15 < i < 85 and 'I' < s[i] < 'M':
            continue
        else:
            t += s[i]
    return t