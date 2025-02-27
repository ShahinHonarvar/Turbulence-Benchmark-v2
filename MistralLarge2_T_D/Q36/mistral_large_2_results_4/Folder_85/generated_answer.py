def filter_chars(s):
    chars_to_remove = set((ch for ch in s[55:80] if 'S' < ch < 's'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))