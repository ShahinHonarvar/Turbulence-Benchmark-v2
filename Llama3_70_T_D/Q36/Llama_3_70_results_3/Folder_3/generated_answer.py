def filter_chars(s):
    s = list(s)
    for i in range(42, 78):
        if s[i] > '!' and s[i] < '?':
            s = [c for c in s if c != s[i]]
    return ''.join(s)