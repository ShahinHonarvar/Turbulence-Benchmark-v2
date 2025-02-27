def filter_chars(s):
    s = list(s)
    for i in range(770, 971):
        if '-' <= s[i] <= 'D':
            s = [c for c in s if c != s[i]]
    return ''.join(s)