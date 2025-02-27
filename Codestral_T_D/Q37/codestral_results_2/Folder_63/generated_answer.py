def filter_chars(s):
    for ch in sorted(set(s[42:93])):
        if '/' <= ch <= 'a':
            s = s.replace(ch, '')
    return s