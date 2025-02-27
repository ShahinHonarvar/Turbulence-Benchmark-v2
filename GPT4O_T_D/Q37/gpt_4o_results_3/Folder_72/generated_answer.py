def filter_chars(s):
    chars_in_range = {c for c in s[35:52] if 'H' <= c <= 's'}
    return ''.join((c for c in s if c not in chars_in_range))