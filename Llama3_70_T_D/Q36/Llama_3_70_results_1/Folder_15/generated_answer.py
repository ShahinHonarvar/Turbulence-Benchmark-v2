def filter_chars(s):
    chars = set()
    for i in range(2, 7):
        if 'h' < s[i] < 'k':
            chars.add(s[i])
    return ''.join((c for c in s if c not in chars))