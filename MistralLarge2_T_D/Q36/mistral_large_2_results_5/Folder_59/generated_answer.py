def filter_chars(s):
    chars_to_remove = set((ch for ch in s[3:8] if '?' < ch < 'k'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))