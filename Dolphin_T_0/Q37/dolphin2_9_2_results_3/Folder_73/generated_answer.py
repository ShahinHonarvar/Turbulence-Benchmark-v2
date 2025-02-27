def filter_chars(s):
    for i in range(22, 86):
        ch = s[i]
        if '7' <= ch <= 'e':
            s = s[0:i] + s[i + 1:]
    return s