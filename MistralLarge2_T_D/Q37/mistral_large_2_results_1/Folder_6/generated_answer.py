def filter_chars(s):
    chars_to_remove = set((ch for ch in s[13:29] if 'c' <= ch <= 'n'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))