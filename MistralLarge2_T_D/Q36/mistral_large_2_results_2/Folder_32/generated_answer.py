def filter_chars(s):
    chars_to_remove = set((ch for ch in s[40:63] if '7' < ch < 'H'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))