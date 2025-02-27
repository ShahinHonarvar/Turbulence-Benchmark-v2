def filter_chars(s):
    chars = set()
    for i in range(27, 86):
        if 'c' <= s[i] <= 'i':
            chars.add(s[i])
    return ''.join((c for c in s if c not in chars))