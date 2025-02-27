def filter_chars(s):
    chars_to_remove = set((ch for ch in s[33:36] if '>' < ch < 'A'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))