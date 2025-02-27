def filter_chars(s):
    chars_to_remove = {c for c in s[35:60] if '!' < c < 'B'}
    return ''.join((c for c in s if c not in chars_to_remove))