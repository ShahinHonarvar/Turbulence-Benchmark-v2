def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 344 <= i <= 874:
            if not 'f' < s[i] < '~':
                t += s[i]
        else:
            t += s[i]
    return t