def filter_chars(s):
    chars_to_remove = set((ch for ch in s[2:7] if 'h' < ch < 'k'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))