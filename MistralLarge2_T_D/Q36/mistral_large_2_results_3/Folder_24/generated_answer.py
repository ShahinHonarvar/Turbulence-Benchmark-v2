def filter_chars(s):
    chars_to_remove = set((ch for ch in s[10:15] if 't' < ch < 'v'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))