def filter_chars(s):
    for c in range(43, 83):
        if s[c] > ':' and s[c] < 'Q':
            s = ''.join([ch for ch in s if ch != s[c]])
    return s