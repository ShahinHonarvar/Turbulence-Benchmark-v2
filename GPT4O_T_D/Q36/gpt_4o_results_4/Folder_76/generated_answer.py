def filter_chars(s):
    chars_to_remove = set()
    for c in s[670:888]:
        if 'B' < c < 'Y':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))