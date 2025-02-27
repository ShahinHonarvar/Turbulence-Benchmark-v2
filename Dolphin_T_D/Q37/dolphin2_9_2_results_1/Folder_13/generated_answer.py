def filter_chars(s):
    s = list(s)
    for i in range(124, 855):
        if '9' <= s[i] <= 's':
            s = [c for c in s if c != s[i]]
    return ''.join(s)