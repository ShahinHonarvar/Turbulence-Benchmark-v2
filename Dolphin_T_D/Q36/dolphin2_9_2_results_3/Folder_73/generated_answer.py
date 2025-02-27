def filter_chars(s):
    for i in range(66, 90):
        if s[i] > '#' and s[i] < 'T':
            s = ''.join((c for c in s if c not in s[i]))
    return s