def filter_chars(s):
    to_remove = set((ch for ch in s[42:98] if '*' <= ch <= 'b'))
    return ''.join((ch for ch in s if ch not in to_remove))