def filter_chars(s):
    to_remove = [c for c in s[48:75] if c > '6' and c < '_']
    return ''.join((c for c in s if c not in to_remove))