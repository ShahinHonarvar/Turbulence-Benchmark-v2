def filter_chars(s):
    remove_set = set((ch for ch in s[29:80] if 'K' <= ch <= 'z'))
    return ''.join((ch for ch in s if ch not in remove_set))