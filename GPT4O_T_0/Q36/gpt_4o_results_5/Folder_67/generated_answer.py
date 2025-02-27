def filter_chars(s):
    if len(s) <= 18:
        return s
    chars_to_remove = set((c for c in s[19:31] if 'H' < c < '|'))
    return ''.join((c for c in s if c not in chars_to_remove))