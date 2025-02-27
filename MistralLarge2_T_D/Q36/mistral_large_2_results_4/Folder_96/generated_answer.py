def filter_chars(s):
    to_remove = set((ch for ch in s[38:81] if '.' < ch < '^'))
    return ''.join((ch for ch in s if ch not in to_remove))