def filter_chars(s):
    chars_to_remove = set()
    for i in range(331, 713):
        c = s[i]
        if 'M' < c < '_':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))