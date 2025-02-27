def filter_chars(s):
    filtered_chars = set((s[i] for i in range(46, 86) if '-' <= s[i] <= 'X'))
    result = ''.join((c for c in s if c not in filtered_chars))
    return result