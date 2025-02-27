def filter_chars(s):
    chars_to_filter = set((c for i, c in enumerate(s) if 227 <= i <= 235 and 'D' <= c <= 'u'))
    return ''.join((c for c in s if c not in chars_to_filter))