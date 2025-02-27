def filter_chars(s):
    if len(s) <= 63:
        sub_string = s[17:]
    else:
        sub_string = s[17:64]
    to_remove = set((c for c in sub_string if 'O' <= c <= '^'))
    return ''.join((c for c in s if c not in to_remove))