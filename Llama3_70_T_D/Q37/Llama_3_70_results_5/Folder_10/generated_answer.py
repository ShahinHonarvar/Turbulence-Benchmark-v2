def filter_chars(s):
    char_set = set(s[63:85])
    char_set = {c for c in char_set if 'E' <= c <= '~'}
    return ''.join((c for c in s if c not in char_set))