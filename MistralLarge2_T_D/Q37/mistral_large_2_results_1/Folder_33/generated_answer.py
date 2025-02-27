def filter_chars(s):
    chars_to_remove = set((ch for ch in s[722:833] if 'K' <= ch <= 'm'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))