def filter_chars(s):
    if len(s) <= 331:
        return s
    chars_to_remove = set()
    for c in s[332:713]:
        if 'M' < c < '_':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))