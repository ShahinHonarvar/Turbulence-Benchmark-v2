def filter_chars(s):
    s = list(s)
    for i in range(221, 420):
        if s[i] > '-' and s[i] < 'v':
            s = [c for c in s if c != s[i]]
    return ''.join(s)