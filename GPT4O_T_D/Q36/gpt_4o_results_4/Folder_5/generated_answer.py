def filter_chars(s):
    if len(s) <= 55:
        return s
    to_remove = {c for c in s[56:66] if 'f' < c < '|'}
    return ''.join((c for c in s if c not in to_remove))