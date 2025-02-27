def filter_chars(s):
    if len(s) < 7:
        return s
    chars_to_remove = set((c for c in s[2:7] if '?' <= c <= 'f'))
    return ''.join((c for c in s if c not in chars_to_remove))