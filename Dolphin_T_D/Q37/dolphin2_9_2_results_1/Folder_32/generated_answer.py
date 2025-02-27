def filter_chars(s):
    s = list(s)
    for i in range(23, 90):
        if 'w' <= s[i] <= '{':
            s = [c for c in s if c != s[i]]
    return ''.join(s)