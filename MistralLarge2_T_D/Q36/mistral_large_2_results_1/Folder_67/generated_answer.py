def filter_chars(s):
    to_remove = set((ch for ch in s[18:31] if 'H' < ch < '|'))
    return ''.join((ch for ch in s if ch not in to_remove))