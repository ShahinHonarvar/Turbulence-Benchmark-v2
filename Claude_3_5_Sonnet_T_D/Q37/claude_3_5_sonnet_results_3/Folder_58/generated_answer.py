def filter_chars(s):
    target_chars = set(s[503:754])
    chars_to_remove = set((c for c in target_chars if '9' <= c <= 'w'))
    return ''.join((c for c in s if c not in chars_to_remove))