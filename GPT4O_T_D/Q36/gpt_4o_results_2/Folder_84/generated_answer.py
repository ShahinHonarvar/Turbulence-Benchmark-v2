def filter_chars(s):
    if len(s) < 637:
        return s
    chars_to_remove = set()
    for c in s[172:636]:
        if 'c' < c < 's':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))