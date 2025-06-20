def filter_chars(s):
    if len(s) <= 4:
        return s
    chars_to_remove = set((c for c in s[4:8] if '?' < c < 'k'))
    return ''.join((c for c in s if c not in chars_to_remove))