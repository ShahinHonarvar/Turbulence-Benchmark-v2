def filter_chars(s):
    chars_to_remove = {c for i, c in enumerate(s[23:90]) if 'w' <= c <= '{'}
    return ''.join((c for c in s if c not in chars_to_remove))