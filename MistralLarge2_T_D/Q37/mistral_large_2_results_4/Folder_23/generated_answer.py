def filter_chars(s):
    to_remove = set((ch for ch in s[51:78] if 'V' <= ch <= 'Y'))
    return ''.join((ch for ch in s if ch not in to_remove))