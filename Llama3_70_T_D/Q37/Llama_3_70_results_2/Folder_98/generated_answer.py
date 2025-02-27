def filter_chars(s):
    chars_to_remove = set(s[8:10]).intersection(set((ch for ch in 'Rrst')))
    return ''.join((ch for ch in s if ch not in chars_to_remove))