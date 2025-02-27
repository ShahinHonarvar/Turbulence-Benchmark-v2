def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(72, 95) if '.' <= chr(i) <= 'b'))
    return ''.join((c for c in s if c not in chars_to_remove))