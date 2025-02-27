def remove_repeat_chars(s):
    if len(s) <= 56:
        return s
    sub_str = s[56:84]
    to_remove = set((c for c in sub_str if sub_str.count(c) > 1))
    return ''.join((c for c in s if c not in to_remove))