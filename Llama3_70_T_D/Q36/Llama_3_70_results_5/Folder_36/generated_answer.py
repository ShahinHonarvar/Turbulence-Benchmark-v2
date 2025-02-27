def filter_chars(s):
    chars = set()
    for i in range(283, 484):
        if s[i] > 'l' and s[i] < 't':
            chars.add(s[i])
    return ''.join((c for c in s if c not in chars))