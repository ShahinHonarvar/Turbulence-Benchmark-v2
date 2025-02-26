def remove_repeat_chars(s):
    target_slice = s[7:9]
    repeat_chars = set((c for c in target_slice if target_slice.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))