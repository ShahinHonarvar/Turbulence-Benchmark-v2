def filter_chars(s):
    chars_to_filter = set((c for i, c in enumerate(s) if 83 <= i <= 99 and '*' <= c <= 'j'))
    return ''.join((c for c in s if c not in chars_to_filter))