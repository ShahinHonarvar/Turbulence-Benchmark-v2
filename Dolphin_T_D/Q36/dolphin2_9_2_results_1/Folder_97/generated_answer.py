def filter_chars(s):
    s = list(s)
    for i in range(309, 591):
        if s[i] > 'S' and s[i] < 'm':
            s = [ch for ch in s if ch != s[i]]
    return ''.join(s)