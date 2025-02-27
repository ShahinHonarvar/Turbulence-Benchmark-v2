def filter_chars(s):
    chars = s[27:86]
    for i in range(len(chars)):
        if 'c' <= chars[i] <= 'i':
            s = s.replace(chars[i], '')
    return s