def filter_chars(s):
    chars_to_remove = set((ch[1] for ch in enumerate(s) if 155 <= ch[0] <= 403 and '(' <= ch[1] <= ']'))
    return ''.join((c for c in s if c not in chars_to_remove))