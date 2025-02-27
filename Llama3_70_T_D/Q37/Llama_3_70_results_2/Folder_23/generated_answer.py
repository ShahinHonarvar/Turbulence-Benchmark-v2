def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(51, 78) if 'V' <= s[i] <= 'Y'))
    return ''.join((c for c in s if c not in chars_to_remove))