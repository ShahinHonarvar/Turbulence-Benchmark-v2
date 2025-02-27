def filter_chars(s):
    to_remove = set((ch for ch in s[41:87] if 'S' <= ch <= 's'))
    return ''.join((ch for ch in s if ch not in to_remove))