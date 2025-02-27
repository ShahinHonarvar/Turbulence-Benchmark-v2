def filter_chars(s):
    if len(s) <= 220:
        return s
    chars_to_remove = {c for c in s[220:403] if '*' < c < '7'}
    return ''.join((c for c in s if c not in chars_to_remove))