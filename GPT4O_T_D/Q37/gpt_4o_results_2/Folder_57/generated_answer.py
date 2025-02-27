def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 27:
        for c in s[27:86]:
            if '!' <= c <= 'B':
                chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))