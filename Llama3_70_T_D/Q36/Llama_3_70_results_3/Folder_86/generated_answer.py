def filter_chars(s):
    to_remove = [c for c in s[672:709] if 'X' < c < '}']
    return ''.join((c for c in s if c not in to_remove))