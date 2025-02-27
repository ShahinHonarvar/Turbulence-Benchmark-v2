def filter_chars(s):
    chars = set()
    for i in range(521, 723):
        if '>' <= s[i] <= '_':
            chars.add(s[i])
    return ''.join((c for c in s if c not in chars))