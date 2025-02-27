def filter_chars(s):
    s = list(s)
    for i in range(63, 85):
        if s[i] >= 'E' and s[i] <= '~':
            s = [c for c in s if c != s[i]]
    return ''.join(s)