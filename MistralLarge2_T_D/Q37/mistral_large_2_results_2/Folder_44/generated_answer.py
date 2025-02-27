def filter_chars(s):
    to_remove = set((ch for ch in s[21:44] if '+' <= ch <= '8'))
    return ''.join((ch for ch in s if ch not in to_remove))