def filter_chars(s):
    chars_to_remove = set((ch for ch in s[18:95] if 'K' < ch < 'a'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))