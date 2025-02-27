def filter_chars(s):
    chars = [s[i] for i in range(225, 382) if s[i] >= 'D' and s[i] <= 'Y']
    for c in chars:
        s = s.replace(c, '')
    return s