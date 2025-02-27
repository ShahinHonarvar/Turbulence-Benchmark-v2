def filter_chars(s):
    s = list(s)
    for i in range(521, 723):
        if s[i] >= '>' and s[i] <= '_':
            s = [c for c in s if c != s[i]]
    return ''.join(s)