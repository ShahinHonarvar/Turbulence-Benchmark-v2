def filter_chars(s):
    for c in range(56, 86):
        if '+' < s[c] < 'w':
            s = ''.join((ch for ch in s if ch != s[c]))
    return s