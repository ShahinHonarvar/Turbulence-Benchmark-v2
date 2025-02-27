def filter_chars(s):
    chars = set()
    for i in range(61, 71):
        if '0' <= s[i] <= '@':
            chars.add(s[i])
    return ''.join((c for c in s if c not in chars))