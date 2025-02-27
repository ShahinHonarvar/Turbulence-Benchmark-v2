def filter_chars(s):
    remove_chars = set((ch for ch in s[348:853] if 'J' <= ch <= 'b'))
    return ''.join((ch for ch in s if ch not in remove_chars))