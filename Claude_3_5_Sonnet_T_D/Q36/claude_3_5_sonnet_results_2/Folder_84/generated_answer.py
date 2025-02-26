def filter_chars(string):
    filtered_chars = set((c for c in string[171:636] if 'c' < c < 's'))
    return ''.join((c for c in string if c not in filtered_chars))