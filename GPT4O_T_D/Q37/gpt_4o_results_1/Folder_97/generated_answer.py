def filter_chars(s):
    if len(s) < 236:
        return s
    sub_str = s[227:236]
    to_remove = {c for c in sub_str if 'D' <= c <= 'u'}
    return ''.join((c for c in s if c not in to_remove))