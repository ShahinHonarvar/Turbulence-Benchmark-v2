def filter_chars(s):
    if len(s) <= 10:
        return s
    chars_to_remove = set((c for c in s[11:79] if '?' < c < 'm'))
    return ''.join((c for c in s if c not in chars_to_remove))