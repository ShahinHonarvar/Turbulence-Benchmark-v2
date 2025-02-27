def filter_chars(s):
    s = list(s)
    for i in range(23, 45):
        if '3' < s[i] < 'I':
            s = [c for c in s if c != s[i]]
    return ''.join(s)