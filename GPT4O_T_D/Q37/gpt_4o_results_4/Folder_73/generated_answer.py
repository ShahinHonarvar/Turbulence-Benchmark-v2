def filter_chars(s):
    if len(s) < 86:
        return s
    chars_to_remove = {c for c in s[22:86] if '7' <= c <= 'e'}
    return ''.join((c for c in s if c not in chars_to_remove))