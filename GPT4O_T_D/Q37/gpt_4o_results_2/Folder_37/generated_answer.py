def filter_chars(s):
    filter_indices = range(17, 64)
    chars_to_remove = {c for c in s[17:64] if 'O' <= c <= '^'}
    return ''.join((c for c in s if c not in chars_to_remove))