def filter_chars(s):
    s = list(s)
    for i in range(26, 65):
        if 'V' <= s[i] <= 'o':
            s = [c for c in s if c != s[i]]
    return ''.join(s)