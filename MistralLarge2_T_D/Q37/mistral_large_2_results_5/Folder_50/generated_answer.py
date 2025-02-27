def filter_chars(s):
    to_remove = set((ch for ch in s[71:97] if '_' <= ch <= 'o'))
    return ''.join((ch for ch in s if ch not in to_remove))