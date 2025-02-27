def filter_chars(s):
    chars_to_remove = set()
    for i in range(71, 97):
        c = chr(i)
        if '_' <= c <= 'o':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))