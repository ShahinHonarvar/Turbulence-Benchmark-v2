def filter_chars(s):
    chars_to_remove = set((ch for ch in s[1:6] if ',' < ch < 'f'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))