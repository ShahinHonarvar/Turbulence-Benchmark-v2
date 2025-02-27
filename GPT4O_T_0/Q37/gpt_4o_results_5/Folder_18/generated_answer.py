def filter_chars(s):
    if len(s) < 771:
        return s
    chars_to_remove = set((c for c in s[770:971] if '-' <= c <= 'D'))
    return ''.join((c for c in s if c not in chars_to_remove))