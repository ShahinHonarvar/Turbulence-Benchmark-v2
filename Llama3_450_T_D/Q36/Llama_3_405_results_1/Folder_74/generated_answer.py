def filter_chars(s):
    chars_to_filter = set((s[i] for i in range(33, 36) if '>' < s[i] < 'A'))
    return ''.join((c for c in s if c not in chars_to_filter))