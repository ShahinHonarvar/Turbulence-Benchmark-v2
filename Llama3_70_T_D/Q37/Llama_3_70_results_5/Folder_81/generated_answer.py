def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(19, 93) if '8' <= s[i] <= 'm'))
    return ''.join((c for c in s if c not in chars_to_remove))