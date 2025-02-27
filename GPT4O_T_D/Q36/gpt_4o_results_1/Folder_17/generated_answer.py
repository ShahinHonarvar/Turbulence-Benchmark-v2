def filter_chars(s):
    remove_chars = {c for c in s[19:95] if 'K' < c < 'a'}
    return ''.join((c for c in s if c not in remove_chars))