def filter_chars(s):
    target_chars = set(s[19:33])
    chars_to_remove = {c for c in target_chars if 'f' <= c <= 'o'}
    return ''.join((c for c in s if c not in chars_to_remove))