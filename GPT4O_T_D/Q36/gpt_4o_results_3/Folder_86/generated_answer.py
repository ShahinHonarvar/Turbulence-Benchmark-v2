def filter_chars(s):
    if len(s) <= 672:
        return s
    chars_to_remove = {c for c in s[673:709] if 'X' < c < '}'}
    return ''.join((c for c in s if c not in chars_to_remove))