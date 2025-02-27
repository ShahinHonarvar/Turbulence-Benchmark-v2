def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(722, 833) if 'K' <= s[i] <= 'm'))
    return ''.join((c for c in s if c not in chars_to_remove))