def filter_chars(s):
    t = set()
    for i in range(31, 70):
        if 'B' < s[i] < 'v':
            t.add(s[i])
    return ''.join((c for c in s if c not in t))