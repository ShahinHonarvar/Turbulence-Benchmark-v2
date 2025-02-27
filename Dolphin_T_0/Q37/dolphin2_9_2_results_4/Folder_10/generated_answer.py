def filter_chars(s):
    to_remove = [c for c in s[63:85] if 'E' <= c <= '~']
    return ''.join([c for c in s if c not in to_remove])