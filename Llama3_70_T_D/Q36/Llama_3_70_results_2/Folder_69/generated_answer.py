def filter_chars(s):
    chars = set()
    for i in range(343, 665):
        if '%' < s[i] < 'U':
            chars.add(s[i])
    return ''.join((c for c in s if c not in chars))