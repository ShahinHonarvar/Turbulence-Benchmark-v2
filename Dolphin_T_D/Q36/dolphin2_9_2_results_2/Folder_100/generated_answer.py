def filter_chars(s):
    for i in range(43, 69):
        if 'B' < s[i] < 'r':
            s = ''.join((c for c in s if c != s[i]))
    return s