def filter_chars(s):
    to_remove = set((ch for ch in s[30:33] if '%' < ch < 'a'))
    return ''.join((ch for ch in s if ch not in to_remove))