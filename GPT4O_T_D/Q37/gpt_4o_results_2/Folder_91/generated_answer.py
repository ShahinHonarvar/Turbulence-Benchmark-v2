def filter_chars(s):
    if len(s) > 8:
        chars_to_filter = {c for c in s[7:9] if 'B' <= c <= 'H'}
        return ''.join((c for c in s if c not in chars_to_filter))
    return s