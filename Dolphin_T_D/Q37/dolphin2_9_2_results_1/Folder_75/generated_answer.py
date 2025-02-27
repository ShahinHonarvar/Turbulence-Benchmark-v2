def filter_chars(s):
    s = list(s)
    for i in range(34, 68):
        if 'W' <= s[i] <= 'x':
            s = [c for c in s if c != s[i]]
    return ''.join(s)