def filter_chars(s):
    chars_to_remove = [c for c in s[3:8] if '?' < c < 'k']
    return ''.join((c for c in s if c not in chars_to_remove))