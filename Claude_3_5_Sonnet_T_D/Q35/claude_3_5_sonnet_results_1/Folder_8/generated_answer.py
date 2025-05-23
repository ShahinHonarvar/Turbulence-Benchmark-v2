def remove_repeat_chars(s):
    if len(s) <= 46:
        return s
    target_slice = s[46:48]
    repeat_chars = set((c for c in target_slice if target_slice.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))