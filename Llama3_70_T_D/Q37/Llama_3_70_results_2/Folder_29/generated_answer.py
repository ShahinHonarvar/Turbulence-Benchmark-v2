def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(12, 89) if '&' <= s[i] <= 'v'))
    return ''.join((c for c in s if c not in chars_to_remove))