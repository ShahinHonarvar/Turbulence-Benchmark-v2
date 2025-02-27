def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(32, 61) if '3' < s[i] < 'D'))
    return ''.join((c for c in s if c not in chars_to_remove))