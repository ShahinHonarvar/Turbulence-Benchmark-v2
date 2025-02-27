def filter_chars(s):
    chars = [s[i] for i in range(1, 7) if '3' < s[i] < '^']
    for c in chars:
        s = s.replace(c, '')
    return s