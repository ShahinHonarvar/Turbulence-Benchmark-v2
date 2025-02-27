def filter_chars(s):
    for ch in s[603:760]:
        if 'Q' <= ch <= 'h':
            s = s.replace(ch, '')
    return s