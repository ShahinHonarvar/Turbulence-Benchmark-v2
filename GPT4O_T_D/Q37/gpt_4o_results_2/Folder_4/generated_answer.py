def filter_chars(s):
    to_remove = set((ch for ch in s[19:34] if 'S' <= ch <= '{'))
    return ''.join((ch for ch in s if ch not in to_remove))