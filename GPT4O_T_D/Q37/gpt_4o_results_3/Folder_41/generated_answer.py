def filter_chars(s):
    filter_indices = s[26:65]
    chars_to_remove = {c for c in filter_indices if 'V' <= c <= 'o'}
    return ''.join((c for c in s if c not in chars_to_remove))