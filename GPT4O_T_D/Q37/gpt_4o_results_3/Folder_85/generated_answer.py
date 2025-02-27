def filter_chars(s):
    if len(s) < 66:
        return s
    to_remove = {c for c in s[28:66] if 'O' <= c <= 'd'}
    return ''.join((c for c in s if c not in to_remove))