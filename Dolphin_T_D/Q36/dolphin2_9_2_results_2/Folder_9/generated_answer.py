def filter_chars(s):
    chars = [s[i] for i in range(50, 92) if 'A' < s[i] < 'Q']
    for c in set(chars):
        s = s.replace(c, '')
    return s