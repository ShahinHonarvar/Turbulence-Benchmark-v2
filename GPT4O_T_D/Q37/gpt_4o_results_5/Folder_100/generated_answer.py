def filter_chars(s):
    if len(s) < 91:
        return s
    char_set = set([c for c in s[88:91] if 'J' <= c <= 'Q'])
    return ''.join((c for c in s if c not in char_set))