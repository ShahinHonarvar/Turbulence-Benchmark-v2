def filter_chars(s):
    if len(s) <= 484:
        return s
    chars_to_remove = set()
    for i in range(284, 484):
        if 'l' < s[i] < 't':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))