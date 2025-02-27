def filter_chars(s):
    indices_to_remove = set((s[i] for i in range(58, 82) if 'F' < s[i] < 'O'))
    return ''.join((c for c in s if c not in indices_to_remove))