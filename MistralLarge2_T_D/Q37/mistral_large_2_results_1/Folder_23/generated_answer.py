def filter_chars(s):
    chars_to_remove = set((ch for ch in s[51:78] if 'V' <= ch <= 'Y'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))