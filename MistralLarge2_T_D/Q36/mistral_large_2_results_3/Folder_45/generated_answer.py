def filter_chars(s):
    chars_to_remove = set((ch for ch in s[81:86] if '!' < ch < 's'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))