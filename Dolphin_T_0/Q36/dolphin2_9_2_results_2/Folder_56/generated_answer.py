def filter_chars(s):
    s = list(s)
    for i in range(31, 50):
        if '/' < s[i] < 'J':
            s = [c for c in s if c != s[i]]
    return ''.join(s)