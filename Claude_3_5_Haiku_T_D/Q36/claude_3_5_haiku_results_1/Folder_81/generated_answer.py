def filter_chars(s):
    chars_to_remove = set(s[52:76] if len(s) > 76 else s[52:])
    chars_to_remove = {c for c in chars_to_remove if '5' < c < 'f'}
    return ''.join((c for c in s if c not in chars_to_remove))