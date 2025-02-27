def filter_chars(s):
    target_chars = set((chr(i) for i in range(ord('!') + 1, ord('*'))))
    filtered_indices = range(83, 93)
    chars_to_remove = set((s[i] for i in filtered_indices if i < len(s) and s[i] in target_chars))
    return ''.join((c for c in s if c not in chars_to_remove))