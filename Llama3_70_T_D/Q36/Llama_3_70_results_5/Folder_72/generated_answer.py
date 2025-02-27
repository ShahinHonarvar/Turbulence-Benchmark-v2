def filter_chars(s):
    chars_to_remove = set()
    for i in range(44, 68):
        c = s[i]
        if 'W' < c < 'x':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))