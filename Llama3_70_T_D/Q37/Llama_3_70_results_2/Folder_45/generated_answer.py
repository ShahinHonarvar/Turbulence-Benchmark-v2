def filter_chars(s):
    s = list(s)
    for i in range(72, 95):
        if i < len(s) and '.' <= s[i] <= 'b':
            s = [c for c in s if c != s[i]]
    return ''.join(s)