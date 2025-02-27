def filter_chars(string):
    chars_to_remove = set((ch for ch in string[41:56] if 'Z' < ch < 'c'))
    return ''.join((ch for ch in string if ch not in chars_to_remove))