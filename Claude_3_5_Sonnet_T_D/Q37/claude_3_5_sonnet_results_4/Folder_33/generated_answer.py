def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 722 <= i <= 832 and 'K' <= c <= 'm'))
    return ''.join((c for c in s if c not in chars_to_remove))