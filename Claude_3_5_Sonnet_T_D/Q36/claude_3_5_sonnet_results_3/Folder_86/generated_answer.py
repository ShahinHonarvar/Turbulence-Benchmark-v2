def filter_chars(string):
    to_remove = set((c for c in string[672:709] if 'X' < c < '}'))
    return ''.join((c for c in string if c not in to_remove))