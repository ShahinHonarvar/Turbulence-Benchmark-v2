def filter_chars(s):
    chars = s[59:82]
    filtered_chars = set((c for c in chars if 'F' < c < 'O'))
    return ''.join((c for c in s if c not in filtered_chars))