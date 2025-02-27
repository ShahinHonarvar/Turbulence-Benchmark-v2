def filter_chars(s):
    chars_to_remove = set(s[3:8])
    return ''.join((c for c in s if c not in chars_to_remove or not '?' < c < 'k'))