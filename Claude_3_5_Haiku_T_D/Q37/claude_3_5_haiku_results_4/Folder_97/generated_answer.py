def filter_chars(s):
    to_remove = set((ch for i, ch in enumerate(s) if 227 <= i <= 235 and 'D' <= ch <= 'u'))
    return ''.join((ch for ch in s if ch not in to_remove))