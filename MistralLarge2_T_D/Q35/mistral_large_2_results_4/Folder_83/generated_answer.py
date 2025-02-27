def remove_repeat_chars(s):
    to_remove = set((c for i, c in enumerate(s) if 100 < i < 200 and s[100:200].count(c) > 1))
    return ''.join((c for c in s if c not in to_remove))