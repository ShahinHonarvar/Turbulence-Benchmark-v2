def filter_chars(s):
    chars = [s[i] for i in range(81, 89) if 'f' < s[i] < '{']
    for c in chars:
        s = s.replace(c, '')
    return s