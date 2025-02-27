def filter_chars(s):
    to_remove = set(s[41:87]) & set('Sabcdefghijklmnopqrs')
    return ''.join((c for c in s if c not in to_remove))