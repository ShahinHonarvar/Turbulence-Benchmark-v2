def filter_chars(s):
    s = list(s)
    chars_to_remove = set((c for i, c in enumerate(s[28:66], 28) if 'O' <= c <= 'd'))
    s = [c for c in s if c not in chars_to_remove]
    return ''.join(s)