def filter_chars(s):
    indices_to_check = s[55:92]
    chars_to_remove = set((ch for ch in indices_to_check if 'J' < ch < 'X'))
    return ''.join((ch for ch in s if ch not in chars_to_remove))