def filter_chars(s):
    target_indices = set(range(42, 93))
    chars_to_remove = set((s[i] for i in range(len(s)) if i in target_indices and '/' <= s[i] <= 'a'))
    return ''.join((c for c in s if c not in chars_to_remove))