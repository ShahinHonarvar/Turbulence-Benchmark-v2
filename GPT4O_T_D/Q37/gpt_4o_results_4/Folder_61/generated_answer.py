def filter_chars(s):
    if len(s) < 7:
        return s
    removal_chars = [c for c in s[5:7] if 'G' <= c <= 'p']
    return ''.join((c for c in s if c not in removal_chars))