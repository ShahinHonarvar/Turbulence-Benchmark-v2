def filter_chars(s):
    special_chars = {c for c in s[155:404] if '(' <= c <= ']'}
    return ''.join((c for c in s if c not in special_chars))