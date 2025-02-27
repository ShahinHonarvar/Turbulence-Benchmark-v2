def filter_chars(s):
    to_remove = set((ch for ch in s[11:46] if '!' < ch < 'A'))
    return ''.join((ch for ch in s if ch not in to_remove))