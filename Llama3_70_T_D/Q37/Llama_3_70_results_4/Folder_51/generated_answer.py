def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(36, 41) if 'H' <= s[i] <= 'e'))
    return ''.join((c for c in s if c not in chars_to_remove))