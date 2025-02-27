def filter_chars(s):
    chars_to_remove = set()
    for c in s[31:73]:
        if 'M' < c < 'j':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))