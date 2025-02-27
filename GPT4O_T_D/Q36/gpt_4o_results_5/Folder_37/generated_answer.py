def filter_chars(s):
    chars_to_remove = {c for c in s[45:59] if '/' < c < '6'}
    return ''.join((c for c in s if c not in chars_to_remove))