def filter_chars(s):
    chars = set((s[i] for i in range(90, 97) if 'j' < s[i] < 'w'))
    return ''.join((c for c in s if c not in chars))