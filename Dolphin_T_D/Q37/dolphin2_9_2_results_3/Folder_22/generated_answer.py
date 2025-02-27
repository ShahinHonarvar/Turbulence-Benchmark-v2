def filter_chars(s):
    chars = [s[i] for i in range(33, 71) if '7' <= s[i] <= 'k']
    for c in chars:
        s = s.replace(c, '')
    return s