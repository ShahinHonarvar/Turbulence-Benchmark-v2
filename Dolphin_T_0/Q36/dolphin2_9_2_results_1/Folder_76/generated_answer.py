def filter_chars(s):
    chars = [s[i] for i in range(669, 888) if 'B' < s[i] < 'Y']
    for c in chars:
        s = s.replace(c, '')
    return s