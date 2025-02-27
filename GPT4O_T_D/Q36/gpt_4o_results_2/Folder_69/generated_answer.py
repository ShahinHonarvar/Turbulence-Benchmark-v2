def filter_chars(s):
    if len(s) <= 343:
        return s
    start = 344 if len(s) > 344 else len(s)
    end = 665 if len(s) > 665 else len(s)
    chars_to_remove = set((c for c in s[start:end] if '%' < c < 'U'))
    return ''.join((c for c in s if c not in chars_to_remove))