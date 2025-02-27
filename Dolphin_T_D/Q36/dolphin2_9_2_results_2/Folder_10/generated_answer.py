def filter_chars(s):
    chars = ''
    for i in range(35, 60):
        if '!' < s[i] < 'B' and s[i] not in chars:
            chars += s[i]
    return ''.join([c for c in s if c not in chars])