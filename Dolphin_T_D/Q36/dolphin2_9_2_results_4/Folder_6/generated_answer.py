def filter_chars(s):
    s = list(s)
    for i in range(31, 70):
        if 'B' < s[i] < 'v':
            s = [c for c in s if c != s[i]]
    return ''.join(s)