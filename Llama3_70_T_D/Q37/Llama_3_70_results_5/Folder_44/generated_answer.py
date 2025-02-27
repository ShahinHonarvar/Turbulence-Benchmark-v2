def filter_chars(s):
    chars = set()
    for i in range(21, 44):
        if '+' <= s[i] <= '8':
            chars.add(s[i])
    return ''.join((c for c in s if c not in chars))