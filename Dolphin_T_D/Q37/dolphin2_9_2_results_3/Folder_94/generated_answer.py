def filter_chars(s):
    s = list(s)
    for i in range(51, 97):
        if s[i] >= 'X' and s[i] <= 'p':
            s = [c for c in s if c != s[i]]
    return ''.join(s)