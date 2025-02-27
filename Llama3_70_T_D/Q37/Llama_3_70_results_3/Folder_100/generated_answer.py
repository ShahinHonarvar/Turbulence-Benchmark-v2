def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(88, 91) if 'J' <= s[i] <= 'Q'))
    return ''.join((c for c in s if c not in chars_to_remove))