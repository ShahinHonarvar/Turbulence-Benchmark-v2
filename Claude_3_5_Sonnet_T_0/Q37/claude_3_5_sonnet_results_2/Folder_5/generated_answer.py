def filter_chars(s):
    chars_to_remove = set((c for i, c in enumerate(s) if 24 <= i <= 82 and '5' <= c <= '<'))
    return ''.join((c for c in s if c not in chars_to_remove))