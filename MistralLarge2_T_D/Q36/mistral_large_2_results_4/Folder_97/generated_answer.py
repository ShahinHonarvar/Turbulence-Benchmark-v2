def filter_chars(s):
    chars_to_remove = {c for c in s[309:591] if 'S' < c < 'm'}
    return ''.join((c for c in s if c not in chars_to_remove))