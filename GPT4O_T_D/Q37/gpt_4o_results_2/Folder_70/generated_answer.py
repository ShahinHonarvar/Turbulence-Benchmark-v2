def filter_chars(s):
    remove_chars = set((c for c in s[515:539] if '+' <= c <= '}'))
    return ''.join((c for c in s if c not in remove_chars))