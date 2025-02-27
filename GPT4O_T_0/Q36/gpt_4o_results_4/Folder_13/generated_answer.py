def filter_chars(s):
    if len(s) <= 323:
        return s
    chars_to_remove = set()
    for c in s[324:526]:
        if ')' < c < 'O':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))